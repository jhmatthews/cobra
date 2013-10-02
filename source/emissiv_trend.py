#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
	University of Southampton -- JM -- 30 September 2013

				plot_emissiv.py 

Synopsis:
	Plot macro atom level emissivities and other information from
	diag file

Usage:
	

Arguments:
'''

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import sys, os, subprocess
import read_output as rd
from constants import *



t_init = 10000.0 # this is the temperatrue of the blackbody
imax = 10 # maximum steps we iterate over
i_temp_steps = 1000  # step widths in temp space

# now we want a list of pywind cmds
# we want to make files 
# we want electron density
# we want neutral hydrogen density and non neutral
#pywindcmds = [ 1, 'n', 't',  'i', 1, 1, 1, 1, 2, 0, 'q']  
pywindcmds = [ 1, 'n', 't', 'q', 'i', 1, 1, 0, 'q']  

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


# empty arrays to append to
hbeta_list= []
matom_emissivities= []
kpkt_emissivities= []
nh_list= []
h1_list= []
ne_list= []
t_e_list = []
hbeta_quantity=[]


# now do the loop over temperature
for i in range(imax):
	
  	# obtain temperature of the star, what we ar eiterating on
	tstar = t_init + (i * i_temp_steps)
	
	# print some info for the user 
	print 'Starting cycle '+str(i+1)+' of '+str(imax) print 'tstar = %lf' % tstar


		   
	# now we open a file for temporary pf, and write to it
	inp =open('input.pf','w')
	inp.write("Wind_type() 9\n")
	inp.write("Atomic_data					   data/h20\n")
	inp.write("photons_per_cycle						   100000\n")
	inp.write("Ionization_cycles							   100\n")
	inp.write("spectrum_cycles								   1\n")
	inp.write("Coord.system()				   0\n")
	inp.write("Wind.dim.in.x_or_r.direction					 4\n")
	inp.write("Wind_ionization()				   3\n")
	inp.write("Line_transfer()					7\n")
	inp.write("System_type()				   0\n")
	inp.write("Star_radiation(y=1)							  1\n")
	inp.write("Disk_radiation(y=1)							  0\n")
	inp.write("Boundary_layer_radiation(y=1)			0\n")
	inp.write("Wind_radiation(y=1)							  0\n")
	inp.write("Rad_type_for_star(0=bb,1=models)_to_make_wind				   0\n")
	inp.write("mstar(msol)									 0.8\n")
	inp.write("rstar(cm)									 1e10\n")
	inp.write("tstar									  %lf\n" % tstar)
	inp.write("disk.type()				   		0\n")
	inp.write("Torus(0=no,1=yes)				0\n")
	inp.write("wind.radmax(cm)				   1.00000000001e11\n")
	inp.write("wind.t.init								10000\n")
	inp.write("shell_wind_mdot(msol/yr)					 0.00472e-19\n")
	inp.write("shell.wind.radmin(cm)					   1e11\n")
	inp.write("shell.wind_v_at_rmin(cm)					1.00000\n")
	inp.write("shell.wind.v_at_rmax(cm)					1.000010\n")
	inp.write("shell.wind.acceleration_exponent				   1\n")
	inp.write("Rad_type_for_star()_in_final_spectrum				  0\n")
	inp.write("spectrum_wavemin 				%f\n" % wavemin)
	inp.write("spectrum_wavemax				%f\n" % wavemax)
	inp.write("no_observers	1\n")
	inp.write("angle(0=pole)	45\n")
	inp.write("phase(0=inferior_conjunction) 	0.5\n")
	inp.write("live.or.die(0).or.extract(anything_else) 1\n")
	inp.write("Select_specific_no_of_scatters_in_spectra(y/n)  	n\n")
	inp.write("Select_photons_by_position(y/n)  	n\n")
	inp.write("spec.type(flambda(1),fnu(2),basic(other)					2\n")
	inp.write("Extra.diagnostics(0=no)						   0\n")
	inp.write("Use.standard.care.factors(1=yes)					1\n")
	inp.write("Photon.sampling.approach()				   3\n")
	inp.close()
	
	
	# pf file created, let's run it
	os.system( "py76c_dev input > output")	
	#subprocess.check_call("tail -n 60 output  | grep MACROOUTPUT > temp",shell=True)


	# run py_wind
	os.system ( "py_wind input < input_comms > pywindout")
	
	# now get the key values from the pywind files
	root = "input"
	h1 = rd.thinshell_read ( root + ".ioncH1.dat" )
	#h2 = rd.thinshell_read ( root + ".ioncH2.dat" )
	ne = rd.thinshell_read ( root + ".ne.dat" )
	t_e = rd.thinshell_read ( root + ".te.dat" )
	#nh = h1 + h2
		
	root = "input"
	rootfolder = "diag_input/"
	matom_emiss, kpkt_emiss = rd.read_emissivity ( rootfolder + root )
	convergence = rd.read_convergence ( rootfolder + root )
	print '\nconvergence fraction = %f' % convergence

	hbeta = matom_emiss[3]
	nlevels_macro = len(matom_emiss)
	n_array = np.arange (nlevels_macro)

	# now append some important values to array
	hbeta_list.append( hbeta )
	hbeta_quantity.append (4.0*PI*hbeta / ne**2)
	matom_emissivities.append ( matom_emiss )
	kpkt_emissivities.append ( kpkt_emiss )
	h1_list.append (h1)
	#nh_list.append( nh )
	#h2_list.append( h2 )
	ne_list.append( ne )
	t_e_list.append( t_e )
	print '\nt_E %8.4e ne %8.4e hbeta %8.4e 4pi j /ne^2 %8.4e h1 %8.4e' % (t_e, ne, hbeta, 4.0*PI*hbeta / ne**2, h1)


# we need to normalise hbeta to be in units of erg cm^-3 s-1



hbeta_list = np.array(hbeta_list)
ne_list = np.array(ne_list)
t_e_list = np.array(t_e_list)
h1_list = np.array(h1_list)

fig = plt.figure()

# number of things to plot
n = 4

# order of things to plot
t_bb = np.arange(t_init, t_init + (imax+1)*i_temp_steps, i_temp_steps)# this is the temperatrue of the blackbody


#pi_hbeta_over_nenep = ( 4.0*PI*hbeta_list / ne_list**2  ) / 1.3e+23
osterbrock = np.array([ 2.7e-25, 1.54e-25, 8.30e-26, 4.21e-26])
t_e_oster =  np.arange(2500, 12500, 2500)

plot_list = [ ne_list, hbeta_quantity, hbeta_list, t_bb]
ylabel = [ 'ne', 'h1', 'hbeta', 'kpkt emissivities']

for i in range(n):
	
	ax = fig.add_subplot( n/2, 2, i)
	
	
	ax.plot(t_e_list, plot_list[i])
	if i ==1: ax.plot(t_e_oster, osterbrock)	
	ax.set_ylabel(ylabel[i])
	
	ax.set_xlabel("Electron Temp")
	
plt.savefig("macro.png")
	

 
'''
hbeta = matom_emiss[3]
#hbeta.append(hbeta)
print hbeta

# scatter plot of level emissivities
plt.suptitle(label)
plt.scatter(n_array, matom_emiss / hbeta)
plt.xlabel( "n" )
plt.ylabel( "Macro atom level emissivities / H_beta level emissivity" )
plt.savefig ( root + "_emissiv.png" )

arr = [86354000.0, 115280000.0, 164750000.0]
temp = [ ]
plt.plot()
'''



