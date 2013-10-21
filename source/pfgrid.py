#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
		pfgrid.py
		
Synopsis:
	Generates a grid of parameter files for the python radiative transfer code.
	Note that this will only generate models with the same general type due to keyword order.

'''




help_string='''
		pfgrid.py
		
Synopsis:
	Generates a grid of parameter files for the python radiative transfer code.
	Note that this will only generate models with the same general type due to keyword order.
	
Usage: 
	pfgrid.py [-h] 

'''
import sys, os
import numpy as np
import astro_func as ast
import pylab


if len(sys.argv)>1:
	if sys.argv[0] == "-h" or sys.argv[0] == "h" or sys.argv[0] == "help":
		print help_string


# read in template file
keywords, values = np.loadtxt('template.pf', dtype='string', unpack=True)

'''# read in grid of values to change
grid = np.loadtxt('grid_values', dtype='string', unpack=True, comments ="#")
keywords_to_change = grid[0]
values_to_change = grid[1:]


nx = len(values_to_change[0])
ny = len(keywords_to_change)


# calculate total number of runs
n_runs = nx ** ny

print "Welcome to pfgrid. Creating grids for %i runs..." % n_runs
print "You have %i variables with %i degrees of freedom" % (ny, nx)

print keywords_to_change

sys.exit()
all_values = []
for i in range(n_runs):
	all_values.append(values)'''
	

# you know have n_runs copies of the initial parameter file
	
#all_values = np.array(values)


# standard alpha of power law
alpha_pl = -0.9





n = 0

MBH = np.array([1.0e9])					# black holes masses
EDD = np.array([0.1, 0.2, 0.5])			# eddington fractions
L_X = np.array([1e43, 1e44, 1e45])		# X-ray luminosities
MDOT_FRAC = np.array([0.1, 1.0, 10.0])	# mdot wind as fraction of mdot acc

# lengths of arrays
nmasses = len(MBH)
nagn = len(L_X)
nwind = len(MDOT_FRAC)
ndisk = len(EDD)

print "Fiducial model:"
print "-----------------------"
m = 1.0e9; mdot = 5.0; lum_agn = 1.0e43
print "L_bol: %8.4e" % ast.L_bol ( mdot, m)

L_2kev = ast.L_two ( lum_agn , -0.9)
L_2500 = ast.L_2500 ( mdot, m )
alpha_ox = ast.alp_ox ( L_2kev, L_2500 )
print "L_2kev: %8.4e   L_2500: %8.4e   alpha_ox: %f" % (L_2kev, L_2500, alpha_ox)

freq_disk, specdisk = ast.spec_disk(1e14,1e18,m,mdot,8.85667e+14,1e17)
print freq_disk, specdisk

pylab.plot ( freq_disk, specdisk )
pylab.show()
print np.sum( specdisk)

for i in range( nmasses):

	m = MBH[i]
	
	for j in range( ndisk):
	
		edd_frac = EDD [j]
		
		mdot = ast.mdot_from_edd ( edd_frac, m )
		
		
		for k in range (nagn):
		
			lum_agn = L_X [k]
		
			for l in range(nwind):
			
				write_array = values
			
				L_2kev = ast.L_two ( lum_agn , -0.9)
				L_2500 = ast.L_2500 ( mdot, m )
				
				alpha_ox = ast.alp_ox ( L_2kev, L_2500 )
				
				print "\nModel %i" % n
				print "-----------------------"
				print "L_2kev: %8.4e   L_2500: %8.4e   alpha_ox: %f" % (L_2kev, L_2500, alpha_ox)
				#print "L_X: %8.4e   L_bol: %8.4e" % (lum_agn, lum_bol)
				
				freq_disk, specdisk = ast.spec_disk(1e14,1e18,m,mdot,8.85667e+14,1e17)
				print np.sum( specdisk)
		
	

				#filename = "run_%i" % n
	
				#np.savetxt(filename, write_array[n], dtype='string', unpack=True)
	
				n += 1 
	









sys.exit()


print "writing to script..."
inp = open("script", "w")
inp.write("#!/bin/bash\n")
inp.write("cd /home/jm8g08/shankar\n")
i = 0
for line in inp:
	root = roots[i]
	inp.write("py76c_dev %s > %s.out &\n" % root)
	i += 1

print "All done!"

''''
for i in range(ny):
	
	constant_keyword = keywords_to_change[i]
	
	for j in range(nx):
		
		keywords_temp = keywords
		values_temp = values 
		
		index_to_array = np.where(keywords == constant_keyword)
		values_temp[index_to_array] = values_to_change
		
	
		 
		all_values_array.append ( values )
		 
		 
		 


# we read a number of arguments from the command line
# the user can decide to change certain keywords
for i in range(len(keywords_to_change)):
	
	keyword = keywords_to_change[i]
	
	for j in range(len(values_to_change[i])):
	
	

		# search keyword array for keyword desired
		index_to_array = np.where(keywords == keyword)
	
		# create an array of values that have a keyword match - should be length 1!!
		value_matches = values[ index_to_array ]

		if len(value_matches)>1:	# if we havemore than one match this an error
			Error('Multiple keyword matches in parameter file!')

		elif len(value_matches)>0:	# if we have one match, change the value
			old_value = value_matches[0]
			new_value = sys.argv[i+1]
			values [index_to_array] = new_value

			print 'Changed keyword %s from %s to %s' % (keyword, old_value, new_value)'''
	
	
