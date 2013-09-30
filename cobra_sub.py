#! /Library/Frameworks/EPD64.framework/Versions/Current/bin/python 
'''
	University of Southampton -- JM -- 30 September 2013

				cobra_sub.py

Synopsis:
	Useful subroutines for the Python radiative transfer code

Usage:
    Use as subroutine
	
Arguments:       
'''

import numpy as np
import classes as cls


def smooth_spectrum( spectrum, smooth_factor ):
    
    # initialise the spectrum array with blank arrays
    smoothed_spectrum = cls.specclass ([],[],[],[],[],[], [], [], []) 
    
    # we don't want to smooth over frequency and wavelength, just shorten them!
    smoothed_spectrum.freq = spectrum.freq
    smoothed_spectrum.wavelength = spectrum.wavelength
    
    # now set the correct elements of the class to be the smoothed_arrays using smooth arrays function
    smoothed_spectrum.emitted = smooth_arrays (spectrum.emitted, smooth_factor)
    smoothed_spectrum.censrc = smooth_arrays (spectrum.censrc, smooth_factor)
    smoothed_spectrum.disk = smooth_arrays (spectrum.disk, smooth_factor)
    smoothed_spectrum.wind = smooth_arrays (spectrum.wind, smooth_factor)
    smoothed_spectrum.scattered = smooth_arrays (spectrum.scattered, smooth_factor)
    smoothed_spectrum.hitsurf = smooth_arrays (spectrum.hitsurf, smooth_factor)
    smoothed_spectrum.spec = smooth_arrays (spectrum.spec, smooth_factor)
    
    return smoothed_spectrum




def smooth_arrays (array, smooth):
    
    '''smooth n arrays with factor smooth according to NSH's method'''

    n = len (array)     # number of arrays to smooth
    bin = float(smooth)     # create a floating point variable
    
    # first we loop over n arrays, index i
    for i in range( n ):
        
        temp1=[]    # temporary array
        
        # now loop over the length of said arrays, index j
        for j in range( len(array[i]) - smooth):
            
            temp=0.0
            
            # now do the smoothing, loop over index k
            for k in range(smooth):
                
                temp = temp + float(array[j+k])
                
            temp1.append ( temp/bin )
                               
        smoothed_array.append(temp1)
        
    return smoothed_array   
    
    
def not_smooth_arrays (array, smooth):
    
    '''smooth n arrays with factor smooth according to NSH's method'''

    n = len (array)     # number of arrays to smooth
    bin = float(smooth)     # create a floating point variable
    
    # first we loop over n arrays, index i
    for i in range( n ):
        
        temp1=[]    # temporary array
        
        # now loop over the length of said arrays, index j
        for j in range( len(array[i]) - smooth):
            
            temp=0.0
            
            # now do the smoothing, loop over index k
            for k in range(smooth):
                
                temp = temp + float(array[j+k])
                
            temp1.append ( temp/bin )
                               
        smoothed_array.append(temp1)
        
    return smoothed_array  