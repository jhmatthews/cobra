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
import disk as ast
import pylab
from disky_const import *



if len(sys.argv)>1:
	if sys.argv[0] == "-h" or sys.argv[0] == "h" or sys.argv[0] == "help":
		print help_string


# read in template file
template = np.loadtxt('template.pf', dtype='string', unpack=True)

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

MBH = np.array([1.0e7, 1.0e8,1.0e9])					# black holes masses
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

#sys.exit()

L_2kev = ast.L_two ( lum_agn , -0.9)
L_2500 = ast.L_2500 ( mdot, m )
alpha_ox = ast.alp_ox ( L_2kev, L_2500 )
print "L_2kev: %8.4e   L_2500: %8.4e   alpha_ox: %f" % (L_2kev, L_2500, alpha_ox)


freq_disk, specdisk = ast.spec_disk(1e14,1e18,m,mdot,8.85667e+14,1e17)

def strip(character, string):
	new_string = ""
	for s in string:
		if s != character:
			new_string += s
	return new_string
	


'''

#print freq_disk, specdisk

pylab.plot ( freq_disk, specdisk )
pylab.show()
print np.sum( specdisk)


sys.exit()
'''
alphas = [[], [], []]
lums = [[], [], []]
lx = [[], [], []]
roots=[]

for i in range( nmasses):

	m = MBH[i]
	
	for j in range( ndisk):
	
		edd_frac = EDD [j]
		
		mdot = ast.mdot_from_edd ( edd_frac, m , eta = 0.1)
		
		
		for k in range (nagn):
		
			Lbol = edd_frac * ast.Ledd(m)
			frac_bh = Lbol / 2.5e46			# scale our L_x with Lbol
			lum_agn = L_X [k] * ( frac_bh)
		
			for l in range(nwind):
			
				mdotwind = MDOT_FRAC[l] * mdot
			
				root = "run%i_edd%.1f_w%.1f_l%i_bh%i" %  ( n, edd_frac, mdotwind, np.log10(lum_agn), np.log10(m) ) 
				root = strip(".", root)
				roots.append(root)
				filename = "%s.pf" % root
				

				
				inp = open(filename, "w")
			
				write_array = template
			
				L_2kev = ast.L_two ( lum_agn , -0.9)
				L_2500 = ast.L_2500 ( mdot , m ) *  np.cos (PI * 40.0 /180.0 )
				
				
				alpha_ox = ast.alp_ox ( L_2kev, L_2500 )
				
				print "\nModel %i %s" % (n, root)
				print "-----------------------"
				print "L_2kev: %8.4e   L_2500: %8.4e   alpha_ox: %f" % (L_2kev, L_2500, alpha_ox)
				print "mdot %8.4e mdotwind %8.4e L_X %8.4e" % (mdot, mdotwind, lum_agn)
				print "L_bol %8.4e" % Lbol
				
				#print "L_X: %8.4e   L_bol: %8.4e" % (lum_agn, lum_bol)'''
				
				'''freq_disk, specdisk = ast.spec_disk(1e14,1e18,m,mdot,8.85667e+14,1e17)
				
				print np.sum( specdisk)'''
		
				index = np.where(write_array[0] == "mstar(msol)")
				write_array [1][ index ] = str ( m )
				
				index = np.where(write_array[0] =="lum_agn(ergs/s) ")
				write_array [1][ index ] = str (lum_agn )
				
				index = np.where ( write_array[0] =="disk.mdot(msol/yr)")
				write_array [1][ index ] = str (mdot)
				
				index = np.where(write_array[0] =="wind.mdot(msol/yr)")
				write_array [1][ index ] = str (mdotwind) 
				

				#filename = "run_%i" % n
				
				write_array = np.transpose ( write_array)
			
				np.savetxt(filename, write_array, fmt="%s\t%s")
	
				n += 1 
	
				alphas[i].append(alpha_ox)
				lums[i].append(L_2500 )		# this is the 40 degree L_2500
				lx[i].append(lum_agn)


lums  = np.array(lums)
#lums = lums * np.cos (PI * 40.0 /180.0 )

colors = ['r', 'g', 'b' ]
labels = ['1e7', '1e8', '1e9']
fit = [ [10.0**27.5, 10.0**32.5], [-1.1, -1.8] ]
import matplotlib.pyplot as plt
fig  = plt.figure()
ax = fig.add_subplot(211)

for i in range(nmasses):
	ax.scatter(lums[i], alphas[i], label=labels[i], c=colors[i])
	
ax.plot(fit[0], fit[1])
ax.set_xscale('log')
ax.set_ylabel("alpha_ox estimate")
ax.set_xlabel("L_2500 estimate")


ax = fig.add_subplot(212)
for i in range(nmasses):
	ax.scatter(lx[i], alphas[i], label=labels[i], c=colors[i])
ax.set_xscale('log')
ax.set_ylabel("alpha_ox estimate")
ax.set_xlabel("L_x")
plt.legend()
plt.savefig("shankar.png")



print "writing to script..."

nscripts = len(roots) / 6.0

# check if there is a remainder
if float(int(nscripts)) != nscripts:
	remainder = len(roots) - ( nscripts * 6)
	nscripts = int(nscripts) + 1
	print nscripts, remainder, len(roots), float(int(nscripts))

for i in range(nscripts):
	inp = open("script%i" % i, "w")
	inp.write("#!/bin/bash\n\n")
	inp.write("cd /home/jm8g08/grid/grid_shankar\n\n")

	first = i*6
	last = (i+1) * 6
	
	if last > len(roots): last = len(roots)
	
	for root in roots[first:last]:
		print root
		inp.write("/home/jm8g08/Python/bin/py76c_dev %s > %s.out &\n" % (root,root))

	
	inp.write("wait\n")
	inp.close()

print "writing to Daddy script..."
inp = open("daddy_script", "w")
inp.write("#!/bin/bash\n\n")
for i in range(nscripts):
	inp.write("qsub -l nodes=1:ppn=6 -l walltime=30:00:00 script%i\n" % i) 

inp.close()
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
	
	
