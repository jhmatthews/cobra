





import matplotlib.pyplot as plt
import pylab
import numpy as np
import classes as cls
import disk as d
import sys, os
import read_output as rd
import bal
from constants import *
from math import fabs

spec = rd.read_spec_file("run110e")

spec_array = bal.flambda_to_fnu (spec.spec[4], spec.freq, spec.wavelength)

BI = bal.BALnicity( C/(1549.0*ANGSTROM), spec.freq, spec_array)

print BI



ls_file = sys.argv[1]
rd.setpars()
filenames = np.loadtxt(ls_file, dtype='string')

bheight = []
bhseven =[]
bhnine =[]

for i in range(len(filenames)):
	spec = rd.read_spec_file (filenames[i])
	spec_array = bal.flambda_to_fnu (spec.spec[4], spec.freq, spec.wavelength)

	BI = bal.BALnicity( C/(1549.0*ANGSTROM), spec.freq, spec_array)
	
	if fabs(BI) > 3000.0:
		if 'bh7' in filenames[i]: bhseven.append(spec)
		if 'bh8' in filenames[i]: bheight.append(spec)
		if 'bh9' in filenames[i]: bhnine.append(spec)
	#pylab.plot(spec.wavelength, spec.spec[4])
	#pylab.xlim(1400,1700)
	#pylab.title(filenames[i])

print len( bhseven) / 24.0
print len( bheight) / 27.0
print len( bhnine) / 27.0

for i in range(len(bhseven)):	
	pylab.plot(bhseven[i].wavelength, bhseven[i].spec[4])
pylab.xlim(1400,1700)
pylab.gca().set_yscale("log")
pylab.xlabel("Flux erg s$^{-1}$ cm$^{-3}$ sr$^{-1}$ $\AA^{-1}$") 
pylab.ylabel("$\lambda, (/AA$)")
pylab.savefig('bh7.png')
pylab.clf()
	
	

for i in range(len(bheight)):	
	pylab.plot(bheight[i].wavelength, bheight[i].spec[4])
pylab.xlim(1400,1700)
pylab.gca().set_yscale("log")
pylab.xlabel("Flux erg s$^{-1}$ cm$^{-3}$ sr$^{-1}$ $\AA^{-1}$")
pylab.ylabel("$\lambda, (/AA$)")

pylab.savefig('bh8.png')
pylab.clf()

for i in range(len(bhnine)):	
	pylab.plot(bhnine[i].wavelength, bhnine[i].spec[4])
pylab.xlim(1400,1700)
pylab.gca().set_yscale("log")
pylab.xlabel("Flux erg s$^{-1}$ cm$^{-3}$ sr$^{-1}$ $\AA^{-1}$") 
pylab.ylabel("$\lambda, (/AA$)")

pylab.savefig('bh9.png')




