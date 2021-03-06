#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
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
import sys


def smooth_spectrum( spectrum, smooth_factor ):
    
    # initialise the spectrum array with blank arrays
    len_specs = len(spectrum.spec[0]) - smooth_factor
    nspecs = len(spectrum.spec)

    dummy = np.array( [ np.arange(len_specs) for i in range(nspecs)] )


    smoothed_spectrum = cls.specclass ([],[],[],[],[],[], [], [], dummy) 
    
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

    for i in range(nspecs):
        smoothed_spectrum.spec[i] = smooth_arrays (spectrum.spec[i], smooth_factor)
    
    return smoothed_spectrum


def smooth(x,window_len=20,window='hanning'):

        if x.ndim != 1:
                raise ValueError, "smooth only accepts 1 dimension arrays."

        if x.size < window_len:
                raise ValueError, "Input vector needs to be bigger than window size."

        if window_len<3:
                return x

        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
                raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"

        s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]


        if window == 'flat': #moving average
                w = np.ones(window_len,'d')
        else:  
                w = eval('np.'+window+'(window_len)')

        y=np.convolve(w/w.sum(),s,mode='same')

        return y[window_len:-window_len+1]



def smooth_arrays (array, smooth):
    
    '''smooth n arrays with factor smooth according to NSH's method'''

    n = len (array)     # number of arrays to smooth
    bin = float(smooth)     # create a floating point variable
    

        
    temp1=[]    # temporary array
        
    # now loop over the length of said arrays, index j
    for j in range( len(array) - smooth):
         
        temp=0.0
            
        # now do the smoothing, loop over index k
        for k in range(smooth):
                
            temp = temp + float(array[j+k])
                
        temp1.append ( temp/bin )
                               
    smoothed_array = temp1
        
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
    










def help_me_spec():
    ''' just a help string for plotting'''
    help_string = '''
	University of Southampton -- JM -- 30 September 2013

				You asked for help!

Synopsis:
	this plots up a spectrum from the Python radiative transfer code

Usage:
    python plot_spec.py root [-s -c -t -a -n]
	
Arguments:
    -s  smoothing factor, otherwise 1 (e.g. -s 20)
    -l  plot common lines on the plot (e.g. -s 20)
    -a  plot a given number of angles (e.g. -a 2 10 27.5)
    -t  use latex labels 
    -h  print this help message
    -c  comparison mode, provide more root files to plot (e.g -c 5, provide 5 root files)
    
exiting.    
'''
    print help_string
    sys.exit() 
    
    
    
    
def help_me_emissivities():
    '''help string for thin shell plotting code'''
    
    help_string='''
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
    value               the value you wish to change it to
    -h                  get this help message and exit
    

'''

    print help_string
    return 0
    
    
    
def print_cobra():
    
    string_to_print = '''             ___.                 
      ____  ____\_ |______________   
    _/ ___\/  _ \| __ \_  __ \__  \  
    \  \__(  <_> ) \_\ \  | \// __ \_
     \___  >____/|___  /__|  (____  /
         \/          \/           \/    
         '''
    print string_to_print
    return 
