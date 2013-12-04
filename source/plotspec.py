#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
Generic plotting script for PYTHONRT

'''


import read_output as rd
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import cobra_sub as sub

rd.setpars()



def strip(character, string):
	''' strip a character from a string'''
	new_string = ""
	for s in string:
		if s != character:
			new_string += s
	return new_string



def plot_spec (filename, lmin, lmax, smooth = 1,  nobs = 0, use = [], \
	           savename = "fig", yscale = "linear", xscale = "linear" , \
	           sources = False, Fnu = False):

	''' 
	Function for plotting a spec file outputted from the radiative transfer code PYTHONRT

	:INPUT:
		filename 			string
							name of file

		lmin, lmax 			float
							wavelength range in ANGSTROMS

		nobs 				int
							number of observes

		smooth				int
							smoothing factor

		use					array
							which observations to use

		savename			string

		yscale, xscale 		string 
							lin or log scale 

		sources 			Bool
		 					Plot sources or not 

		Fnu 				Bool
		 					Is it an Fnu plot?


	:OUTPUT:
		Creates plot and opens in preview 
	'''


	# default savename is filename
	if savename == "fig":
		savename = filename + ".png"


	# create spec class from spec file
	spec = rd.read_spec_file(filename)

	if nobs == 0:
		nobs = len(spec.spec)

	# strip filenames of funny characters that TeX complains about
	savename = strip("_", savename)
	filename = strip("_", filename)


	# default argument is to plot all observations
	if len(use) == 0:
		use = np.arange(nobs)

	nuse = int(len(use))

	# work out the dimensions of the plot
	if nuse < 3:
		ny = nuse
		nx = 1
	else:
		nx = 2
		ny = (len(use) + 1) / 2


	# do we want to smooth? if so, do it!
	if smooth > 1:
		for i in use:
			sub.smooth_spectrum( spec, smooth )


	# now create figure
	fig=plt.figure(figsize=(8.3,11.7),dpi=80)
	fig.suptitle(filename,fontsize=24,fontweight='bold')
	fig.subplots_adjust(hspace=0.3,wspace=0.2)


	for i in range(nuse):

		ax = fig.add_subplot( ny, nx, i)

		if Fnu:
			ax.plot(spec.freq, spec.spec[use[i]])
		else:
			ax.plot(spec.wavelength, spec.spec[use[i]])

		ax.set_yscale(yscale)
		ax.set_xscale(xscale)

		plt.xlim(lmin, lmax)


	plt.savefig(savename)

	command = "open -a preview %s" % savename

	os.system(command)

	if sources:
		fig=plt.figure(figsize=(8.3,11.7),dpi=80)
		fig.suptitle(filename,fontsize=24,fontweight='bold')
		fig.subplots_adjust(hspace=0.3,wspace=0.2)


	return 0






filename = sys.argv[1]
nobs = int(sys.argv[2])


plot_spec(filename, 3000, 7000, smooth = 20, yscale = "log")







