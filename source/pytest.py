#! /Library/Frameworks/Python.framework/Versions/Current/bin/python
'''
	University of Southampton- JM- 22 August 2013

				pytest.py

Synopsis:
	pytest.py is the script which governs regression testing in python
	it has a number of subroutines it uses.
    
    Note that to use this script you must have the environment variable 
    $NIGHTLY_PYTEST defined

Usage:
	python pytest.py -path [path/to/version] -m [mode] -f [custom_filename for mode 4]

Arguments:

	-m mode
		the mode you want to test
		0- just check compilation (default)
		1- just check python runs (nightly)
		2- standard regression test (weekly)
		3- long regression test (prerelease)
		4- custom set of files

	-path [path/to/version]
		the folder of the version you want to test.
		default is $PYTHON/progs/python_dev/	
'''

# import modules we want to use
import numpy as np
import matplotlib.pyplot as plt
import os, sys, subprocess
from sub_report import *
import pytest_sub as sub
import datetime, subprocess, time


# first we want to decide what mode the user wants to operate in
COMPILE = 0		## mode 0: just check compilation
SIMPLE = 1		## mode 1: just check python runs (nightly)
STANDARD = 2		## mode 2: standard regression test (weekly)
RELEASE = 3		## mode 3: long regression test (prerelease)
CUSTOM = 4		## mode 4: custom set of filenames provided in file as argument


## if the values aren't read then these are kept as True




# read arguments and apply
arguments = sys.argv
mode, path_to_folder, custom_filename = sub.read_args(arguments)


send_failure_email()

# now we have read arguments from user
# next step is to download python and test
dir_command = 'cd '+ path_to_folder
git_command = 'git checkout dev; git pull origin dev'
make_command = 'make clean; make python; make clean'

# pull changes from origin/dev to local machine
try:
	sub.execute_commands( [dir_command, git_command] )	## executes commands in a list one after the other
except:
	Error_warning('could not pull from remote git repository. Using local version') ## warns user if can't pull


# now attempt to compile python
try:
	print 'Attempting to compile Python...'
	sub.execute_commands( [dir_command, make_command] )	## executes commands in a list one after the other
except:
	send_failure_email()
	Error('could not compile Python. Reporting to user and exiting.')


## if python compiled and got this far then the compilation test is passed...
## print time to logfile on dropbox and exit
log_filename = '$NIGHTLY_PYTEST/logs/compilation_logfile'



if mode == COMPILE:
	check_file_length (log_filename, 100)		## this truncates the length of the logfile if too long
	now = datetime.datetime.now()
	time_string = str(now)
	log_string =  time_string +': Compilation test passed.'
	os.system('echo '+log_string+' >> '+log_filename)
	copy_file_to_web(log_filename)
	print 'Python compiled ok, Exiting.'
	sys.exit(0)



#output = os.system('cd $NIGHTLY_PYTEST/tests; py76c_dev svtest_1 > svtest_1.out &')



## if we are in simple mode we just want to check a simple run finished and quit
if mode == SIMPLE:
	check_file_length (log_filename, 100)		## this truncates the length of the logfile if too long
	now = datetime.datetime.now()
	time_string = str(now)
	log_string =  time_string +': Compilation and simple run test passed.'
	os.system('echo '+log_string+' >> '+log_filename)
	copy_file_to_web(log_filename)
	print 'Python ran a simple test and completed. Exiting.'
	sys.exit(0)


# this next section submits a job to iridis. We should now exit, we will run the processing script a number of hours later
USER = "jm8g08"
HOST = "iridis3_c.soton.ac.uk"
PASS = "111Neverlose"


# our first job is to go to python_dev and compile the latest commit
COMMAND = '''module load mpich2/1.4.1/gcc;
cd $PYTHON/progs/python_dev/; git checkout dev; git pull origin dev;
make clean; make python; make clean;
'''
sub.run_remote_command ( HOST, COMMAND, USER, PASS )


# now submit the job
COMMAND= "cd /home/jm8g08/nightly_regression_tests/; qsub -l nodes=1:ppn=8 -l walltime=10:00:00 /home/jm8g08/nightly_regression_tests/iridis_nightly_script"
sub.run_remote_command ( HOST, COMMAND, USER, PASS )



# we now want the thread to go to sleep until iridis is done
time_to_sleep = (3600 * 8) + 60 # 8 hours plus a minute grace period
time.sleep(time_to_sleep)



#-----SLEEP OVER, TIME TO POST PROCESS --------

#now iridis should be finished, so we can process the data



# this next loop creates an array of stuff we need - spectra, wind saves and diag files!
extensions_need = [".spec", ".wind_save"]
for pf in pf_files:
    files_i_need.append("diag_"+pf+"/"+pf+"_0/diag")    # append the 0th thread diag file
    for extension in extensions_needed:
        string = pf + extension
        files_i_need.append(string)



for file in files_i_need:
    # get all the outputs from iridis
    os.system("python $NIGHTLY_PYTEST/scripts/scphost.py get iridis nightly_regression_tests/"+file+" outputs/")
    
    
# we should now have all the correct output files needed to process stuff
for pf in pf_files:
    # create the spectrum comparison plot
    os.system("python $NIGHTLY_PYTEST/scripts/spec_compare.py templates/"+pf+"outputs"+pf+" 20 -c nolines sources")
    
    # move all the jpg files into the plots folder
    os.system("mv *jpg $NIGHTLY_PYTEST/plots/")
    

# this script creates the latex file    
os.system("python $NIGHTLY_PYTEST/scripts/makelatex.py")     

# this puts the latex file online
copy_file_to_web('$NIGHTLY_PYTEST/tests/figures_test_76c.pdf')



## if we are in simple mode we just want to check a simple run finished and quit
if mode == STANDARD:
	print 'Python completed standard regression test. Exiting.'
	sys.exit(0)





