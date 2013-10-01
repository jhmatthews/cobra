#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
	University of Southampton -- JM -- 30 September 2013

				read_output.py

Synopsis:
	this plots up a spectrum from the Python radiative transfer code

Usage:
    python plot_spec.py root [-s -c -t -a -n]
	
Arguments:
    -s  smoothing factor, otherwise 1 (e.g. -s 20)
    -l  plot common lines on the plot (e.g. -s 20)
    -a  plot a given number of angles (e.g. -a 2 10 27.5)
    -h  print this help message
    -c  comparison mode, provide more root files to plot (e.g -c 5, provide 5 root files)
    
    
'''



# first import modules of use
import csv, sys, os, array, warnings
import matplotlib.pyplot as plt
import numpy as np
import read_output as rd
import cobra_sub as sub

sub.print_cobra()

# filename is provided by command line
print 'Reading your commands from command line'
mode, store = rd.read_args (sys.argv)

print 'Welcome to cobra, the plotting utility for the radiative transfer code, Python.'
rd.setpars() #this just sets some standard parameters, e.g. tex

# if user asked for help we print help message and exit
if mode.help:
    sub.help_me_spec()

filename = store.filename

# read the spec file
spectrum = rd.read_spec_file (filename)



# we now want to smooth our spectrum
smooth = store.ibin
sub.smooth_spectrum(spectrum, smooth)


# now plot up
fig=plt.figure(figsize=(8.3,11.7),dpi=80)
fig.suptitle(fname,fontsize=24,fontweight='bold')
fig.subplots_adjust(hspace=0.3,wspace=0.2)

ax.plot(spectrum.wavelength, spectrum.spec[0])
plt.show()





'''
bin=float(ibin)
smoothtempspec=[]


for i in range(len(tempspec)-ibin):
	temp1=[]
	for j in range(nobs):
		temp=0.0
		for k in range(ibin):
			temp=temp+float(tempspec[i+k][j])
		temp1.append(temp/bin)
	smoothtempspec.append(temp1)


spec=np.transpose(tempspec)
smoothspec=np.transpose(smoothtempspec)

ny=nobs/2


fig=plt.figure(figsize=(8.3,11.7),dpi=80)
fig.suptitle(fname,fontsize=24,fontweight='bold')
fig.subplots_adjust(hspace=0.3,wspace=0.2)
plt.rcParams['font.size']=8

#	ax.axis([wavelength[len(wavelength)-1],wavelength[0],0,fmax])




for i in range(nobs):
	ax=fig.add_subplot(ny+1,2,i+1)
	plt.xlim(lmin,lmax)
	ax.set_title(titles[8+i],fontsize=14)
	ax.plot(wavelength[0:-ibin],smoothspec[i])
	ax.axvline(x=1550)
        plt.text(1550,fmin[i],'CIV',fontsize=6)
	ax.axvline(x=1032)
	ax.axvline(x=1038)
        plt.text(1038,fmin[i],'OVI',fontsize=6)	
	ax.axvline(x=1239)
	ax.axvline(x=1243)
        plt.text(1243,fmin[i],'NV',fontsize=6)
	ax.axvline(x=1394)
	ax.axvline(x=1403)
        plt.text(1403,fmin[i],'SiIV',fontsize=6)


plt.savefig(sys.argv[1]+'spectrum_summary.jpg',dpi=80,facecolor='w',edgecolor='w',orientation='portrait')

'''




