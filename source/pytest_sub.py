############################################################	
#					pytest_sub.py
#
# pytest_sub is a subroutine which contains functions to deal 
# with testing Python
#
############################################################

import os
import numpy as np
from sub_report import *

def read_args(arg_array):
	mode_default = True
	path_default = True
	no_custom = True
	if len(arg_array) > 1 and len(arg_array) < 8:
		for i_option in range(len(arg_array)):
			if arg_array[i_option] == '-path': 
				path_to_version = arg_array[i+1]
				path_default = False
			if arg_array[i_option] == '-m': 
				mode = int(arg_array[2])
				mode_default = False
			if arg_array[i_option] == '-f':
				custom_filename = arg_array[i+1]
				no_custom = False
		if mode == 4 and no_custom == True:
			print 'Error: mode 4 but no filename provided, exiting'
			
	elif len(arg_array) == 1:
		print 'Usage: python pytest.py -path [path/to/version] -m [mode]' 
		print 'Warning: No arguments supplied'
	else:
		print 'Usage: python pytest.py -path [path/to/version] -m [mode]' 
		print 'Warning: Detected more arguments than expected.'

	## if no arguments read, resort to defaults
	if mode_default:
		print 'setting mode to 0, compilation only'
		mode = 0
	if path_default:
		python_dir = os.system('echo $PYTHON')
		path_to_folder = '$PYTHON/progs/python_dev/'
		print 'Using version of python in folder $PYTHON/progs/python_dev/ as default'
	if no_custom:
		custom_filename =''

	return mode, path_to_folder, custom_filename





'''
execute_commands ( command_array )
	this function simply executes a series of commands in a row
	the commands are passed to the function as an array
'''
def execute_commands ( command_array ):
	all_commands = command_array[0]
	for comm in command_array[1:]:
		all_commands = all_commands + '; '+ comm
	print all_commands
	os.system( all_commands )	## execute the commands

'''
get_version(folder) 
	this function reads version.h in the required folder
	post compilation so python knows which binary to run
'''

def get_version(folder):
	version_text = np.loadtxt ( folder + "version.h", unpack = True)
	print version_text
	version = version_text [0] [2]
	return version
	#define VERSION  "76b_dev"
#define CHOICE 1 // Compress plasma as much as possible



'''
run remote_command
	this function executes a series of commands on a host
'''

def run_remote_command ( host, command, username, password):
	import pexpect
	FULL_COMMAND = "ssh %s@%s %s" % (username, host, command)
	child = pexpect.spawn(FULL_COMMAND)
	child.expect('password:')
	child.sendline(password)
	child.expect(pexpect.EOF)
	



