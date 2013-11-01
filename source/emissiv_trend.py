#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
    University of Southampton -- JM -- 30 September 2013

				plot_emissiv.py 

Synopsis:

	Plot macro atom level emissivities and other information from
	diag file for a variety of temperatures
    
    This code sets up a thin shell model with an illuminating blackbody.
    It then iterates over black body temperature to alter the electron
    temperature 

Usage:
    emissiv_trend.py [keyword to change] [value] [-h]
    
    uses a file template.pf to provide the base model
	
Arguments:
    keyword_to_change   the keyword in the pf file you wish to modify
    value   the value you wish to change it to
    -h      get this help message and exit
    

'''

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import sys, os, subprocess
import read_output as rd
from constants import *
from sub_report import *
import cobra_sub as cobra

nargs = len(sys.argv)
if nargs>1:
    for i in range(len(sys.argv)):
        if sys.argv[i]=='-h' or sys.argv[i]=='h' or sys.argv[i]=='help':
            cobra.help_me_emissivities()
            sys.exit()
    


# print out a big cobra sign!
cobra.print_cobra()



# we iterate over blackbody temperatire
t_init = 10000.0 # this is the starting temperture of the blackbody
imax = 10 # maximum steps we iterate over
i_temp_steps = 1000  # step widths in temp space
MACRO = 7
MACRO_ISO=6


# now we want a list of pywind cmds
# we want to make files 
# we want electron density
# we want neutral hydrogen density and non neutral
#pywindcmds = [ 1, 'n', 't',  'i', 1, 1, 1, 1, 2, 0, 'q']  
pywindcmds = [ 1, 'n', 't', 'i', 0, 1, 1, 0, 'q']  

# first write these commands to a file
inp =open('input_comms','w')

for command in pywindcmds:
	inp.write ( "%s\n" % str(command) )
inp.close()	

 
rd.setpars()	# set standard plotting parameters, e.g. tex






# set the band you want to plot emissivities over
# 3000-7000 will get the balmer continuum
wavemin = 3000.0
wavemax = 7000.0




# we read from a template file template.pf
print 'Reading template parameter file'
keywords, values = np.loadtxt('template.pf', dtype='string', unpack=True)




# we read a number of arguments from the command line
# the user can decide to change certain keywords
for i in range(len(sys.argv)):
	keyword = sys.argv[i]

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

		print 'Changed keyword %s from %s to %s' % (keyword, old_value, new_value)
	




# now get the line transfer mode	
mode = int (values[ np.where(keywords == 'Line_transfer()') ][0])
if mode == MACRO or mode==MACRO_ISO:
	print 'Working with macro atom line transfer so turning on emissivitiy diagnostics'


# empty arrays to append to
hbeta_list= []
matom_emissivities= []
kpkt_emissivities= []
nh_list= []
h1_list= []
ne_list= []
t_e_list = []
hbeta_quantity=[]
halpha_over=[]
t_bb=[]

print 'Mass loss rate is ', values[ np.where(keywords == 'shell_wind_mdot(msol/yr)') ][0]

# now do the loop over temperature
for i in range(imax):
	
  	# obtain temperature of the star, what we ar eiterating on
	tstar = t_init + (i * i_temp_steps)
	
	# print some info for the user 
	print 'Starting cycle '+str(i+1)+' of '+str(imax) 
	print 'tstar = %lf' % tstar


		   
	# now we open a file for temporary pf, and write to it
	inp =open('input.pf','w')

	# cycle through keywords and write to file
	for j in range(len(keywords)):
	
		# if the keyword is tstar then we are iterating over it
		if keywords[j] == 'tstar':
			inp.write("tstar		%lf\n" % tstar)

		# if not just write the value stored in the values array
		else:
			inp.write('%s    %s\n' % (keywords[j], values[j]))

	# close file
	inp.close()
	
	
	# pf file created, let's run it using latest vers
	os.system( "py76c_dev input > output")

	# define root names
	root = "input"
	rootfolder = "diag_input/"


	# check convergence 
	convergence = rd.read_convergence ( rootfolder + root )
	print 'convergence fraction = %f' % convergence

	# if we are converged, do diagnositcs
	if convergence ==1.0:

		# run py_wind
		os.system ( "py_wind input < input_comms > pywindout")

		# get important values from py_wind
		h1 = rd.thinshell_read ( root + ".ionH1.dat" )	# fraction of h1
		ne = rd.thinshell_read ( root + ".ne.dat" )
		t_e = rd.thinshell_read ( root + ".te.dat" )
		
		if h1 < 0.02: # check if the model is ionised
			# now append the values for hydrogen density, 
			# ne and electron temp as well as BB temp
			h1_list.append (h1)
			ne_list.append( ne )
			t_e_list.append( t_e )
			t_bb.append(tstar)

			# now append some important macro atom values to array

			if mode == MACRO or MACRO_ISO:

				# read emissivities from diag file
				matom_emiss, kpkt_emiss = rd.read_emissivity ( rootfolder + root )
	
				# get hbeta level emissivity
				hbeta = matom_emiss[3]
				nlevels_macro = len(matom_emiss)

				n_array = np.arange (nlevels_macro)

				# now append values to array
				hbeta_list.append( hbeta )
				hbeta_quantity.append ( hbeta / (1.3e23 * ne**2) )	# quantity from osterbrock
				halpha_over.append ( matom_emiss[2] / hbeta )	# ratio of H alpha to H beta

				# append the actual level emissivities
				matom_emissivities.append (matom_emiss)
				kpkt_emissivities.append (kpkt_emiss)

				print "\nt_E %8.4e ne %8.4e hbeta %8.4e 4pi j /ne^2 %8.4e h1 %f\n" % (t_e, ne, hbeta, 4.0*PI*hbeta / (2.3e23 * ne**2)  , h1)
	
		else:
			print 'Non ionised model...'

	else:
		print 'Non Converged model...'



# we need to normalise hbeta to be in units of erg cm^-3 s-1


hbeta_list = np.array(hbeta_list)
halpha_over = np.array(halpha_over)
ne_list = np.array(ne_list)
t_e_list = np.array(t_e_list)
h1_list = np.array(h1_list)

fig = plt.figure()


# order of things to plot
#t_bb = np.arange(t_init, t_init + (imax)*i_temp_steps, i_temp_steps)# this is the temperatrue of the blackbody


#pi_hbeta_over_nenep = ( 4.0*PI*hbeta_list / ne_list**2  ) / 1.3e+23



# we need to define arrays of the predicted values from Osterbrock

# first the array of temperatures Osterbrock gives- just a short range
t_e_oster =  [2500.0, 5000.0, 10000.0, 20000.0]

# now line intensities
oster_h_beta_absolute =  np.array  ([ 2.7e-25, 1.54e-25, 8.30e-26, 4.21e-26])  # 4pi j_hbeta / ne **2 values
oster_h_alpha_relative = np.array ([ 3.42, 3.10, 2.86, 2.69])	# ratios of halpha to hbeta from osterbrock
oster_h_gamma_relative = np.array ([ 0.439, 0.458, 0.470, 0.485]) # ratios of hgamma to hbeta from osterbrock
oster_h_delta_relative = np.array ([ 0.237, 0.25, 0.262, 0.271])  # ratios of hdelta to hbeta from osterbrock
oster_p_alpha_relative = np.array ([ 0.684, 0.562, 0.466, 0.394])  # ratios of palpha to hbeta from osterbrock


# if we are in macro mode we want to plot lots of things
if mode == MACRO or mode==MACRO_ISO:
	plot_list = [ halpha_over, hbeta_quantity, hbeta_list, t_bb]
    
	oster_list = [ oster_h_beta_absolute, oster_h_gamma_relative, oster_p_alpha_relative ]
    
    # we need some raw latex strings for labels
	ylabel = [ r'$H \alpha / H \beta$', r'$4\pi j_{H \beta} / n_e^2$', r'$H \beta$', '$T_{bb}$']

# if we aren't in macro mode we on;y want to plot a few things
else: 
	plot_list = [ ne_list, t_bb]
	ylabel = [ '$n_e$', '$T_{bb}$']



# number of things to plot
n = len(plot_list)


for i in range(n):
	
	ax = fig.add_subplot( n/2, 2, i+1)
	
	print i
	ax.plot(t_e_list, plot_list[i], c='b')
	if i ==0: 
		ax.plot(t_e_oster, oster_h_alpha_relative)	
	if i ==1: 
		ax.plot(t_e_oster, oster_h_beta_absolute)	
	ax.set_ylabel(ylabel[i])
	
	ax.set_xlabel(r"$T_e$ (K)")
	



# finally, save the figures	
if mode == MACRO:
	plt.savefig("macro.png")
else:
	plt.savefig("nonmacro.png")
    
    
    
    
    
    

