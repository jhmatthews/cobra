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
fig = plt.figure()
i_plot = 0
for i in range(1, len(sys.argv)):

	root = sys.argv[i]
	#label = sys.argv[i+1]
	
	
	if 'cab' in root:
		seaton =[[2.71, 1.00, 0.506, 0.298, 0.192, 0.132, 0.095, 0.071], \
		 [2.79, 1.00, 0.491, 0.282, 0.178, 0.120, 0.085, 0.063]]
		 
		oster_case_b = [[2.87, 1.00, 0.466, 0.256, 0.158, 0.105, 0.073, 0.0529] , \
		                [2.76, 1.00, 0.474, 0.262, 0.162, 0.107, 0.074, 0.0538]]
	else:
		seaton = [[1.91, 1.00, 0.589, 0.378, 0.258, 0.184, 0.137, 0.104], \
	          [1.99, 1.00, 0.569, 0.356, 0.238, 0.167, 0.122, 0.092]]
		

	rootfolder = 'diag_%s/' % root

	matom_emiss, kpkt_emiss = rd.read_emissivity ( rootfolder + root )

	nlevels_macro = len(matom_emiss)
	n_array = np.arange (nlevels_macro)
	n_array = n_array+1.0
	rd.setpars()    # set standard plotting parameters

	hbeta = matom_emiss[3]
	#hbeta.append(hbeta)
	print hbeta

	label = "Case A" 
	# scatter plot of level emissivities
	if 'cab' in root: label = "Case B" 

	ax = fig.add_subplot(2,1,i_plot+1)
	plt.text(9,1,label)
	ax.scatter(n_array, matom_emiss / hbeta,  label = '\\textsc{Python}', s=80, edgecolors='k', facecolors='none')
	ax.scatter(n_array[2:10], seaton[i_plot], label = 'Seaton (1959)',s=20, color='k')
	#if 'cab' in root:
	#	ax.scatter(np.arange(3,11), oster_case_b[i_plot], label="Osterbrock", c='r', s=10)
	if i==2: ax.set_xlabel( "$n_{upper}$" )
	ax.set_ylabel( r"Balmer decrement ($F_n$ / $F_{\beta}$)" )
	plt.xlim(2.5,10.5)
	plt.ylim(0,3)
	if i ==1: plt.legend()
	i_plot+=1




plt.savefig ( "seaton_emissiv.png" )


#arr = [86354000.0, 115280000.0, 164750000.0]
#temp = [ ]
#plt.plot()




