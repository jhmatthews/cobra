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

root = sys.argv[1]

matom_emiss, kpkt_emiss = rd.read_emissivity ( root )

nlevels_macro = len(matom_emiss)
n_array = np.arange (nlevels_macro)


rd.setpars()    # set standard plotting parameters

# scatter plot of level emissivities
plt.scatter(n_array, matom_emiss)
plt.xlabel( "n" )
plt.ylabel( "Macro atom level emissivities" )
plt.savefig ( root + "_emissiv.png" )





