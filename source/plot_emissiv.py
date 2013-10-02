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

label = sys.argv[2]



rootfolder = 'diag_%s/' % root

matom_emiss, kpkt_emiss = rd.read_emissivity ( rootfolder + root )

nlevels_macro = len(matom_emiss)
n_array = np.arange (nlevels_macro)


rd.setpars()    # set standard plotting parameters

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




