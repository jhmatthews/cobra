

from constants import *
import pylab
import numpy as np
from math import fabs


def vel_nu (nu, nu_0):
	'''
	Returns the velocity of a frequency nu with respect to 
	line centre nu_0 in units of cm/s
	'''
	delta_nu = nu - nu_0
	
	vel = C * delta_nu / nu_0
	
	return vel
	

def nu_vel(v, nu_0):
	'''
	Returns the frequency of a velocity v with respect to 
	line centre nu_0 in units of cm/s
	'''
	
	nu =  (nu_0 * v / C) + nu_0
	
	return nu
	




def mean_with_ignore(x,delta_ignore):
	"""take the mean, then ignore points, x_i that satisfy (x_i-mean)/mean>delta. if delta_ignore=0 use original mean."""
	sum_over_x=sum(x)
	mean_x=( 1.0 * sum(x) )  /  ( 1.0 * len(x) )
	x_no_outliers=[]
	if delta_ignore!=0:
		for i in range(len(x)):
			test_val= fabs(x[i] - mean_x)/mean_x
			
			if test_val <= delta_ignore: x_no_outliers.append( x[i] )	
		mean_no_outliers=( 1.0 * sum(x_no_outliers) )  /  ( 1.0 * len(x_no_outliers) )
		return mean_no_outliers
	else: 
		return mean_x


def normalise(x, delta, normalise_point = 0):
	"""normalise data so 1=mean (including ignoring any outliers if specified. if delta_ignore=0 use original mean."""
	x_normalised=[]
	if normalise_point ==0:
		mean_norm=mean_with_ignore(x,delta)
	
	else:
		mean_norm = x[normalise_point]
	for i in range(len(x)):
		x_norm= 1.0 * x[i] / mean_norm
		x_normalised.append(x_norm)
	return x_normalised
	

		
def BALnicity ( nu_line, nu_array, spec_array):

	'''
	calculate the BALnicity index of a line
	
	:INPUT
		nu_line		float
					The frequency of the line at line centre
		
		nu_array		float
					array of frequencies
		
		spec_array	float
					array of intensities/fluxes
		
	:OUTPUT
		BALnicity index		float
		
	'''
	
	# we integrate over positive velocities as looking for blueshifted BALs
	
	vlow = 3000.0*1.0e5		# need to give velocity in CGS units
	nu_low = nu_vel(vlow, nu_line)
	
	vhigh = 25000.0*1.0e5
	nu_high = nu_vel(vhigh, nu_line)
	
	ilow = 0; ihigh = -999
	
	for i_nu in range(len(nu_array)):
		 if nu_array[i_nu]>= nu_low and ilow==0:
		 	ilow = i_nu
		 	ihigh = 0
		 
		 if nu_array[i_nu]>= nu_high and ihigh==0:
		 	ihigh = i_nu
		 

	spec_array = normalise(spec_array, 0.05, normalise_point=682)
	
	constants = np.zeros(len(spec_array))
	
	for i in range(ilow, ihigh):
		if spec_array[i] <= 0.9: 
			constants[i] = 1
			
	#pylab.plot(nu_array[ilow:ihigh], spec_array[ilow:ihigh])
	
	#pylab.show()
	
	BI = 0.0	
	for i in range(ilow, ihigh):
		dv = ( vel_nu(nu_array[i], nu_line) - vel_nu(nu_array[i-1], nu_line) )
		contribution = constants[i] * ((1.0 - (spec_array[i] / 0.9)) * dv)

		BI += contribution
	
	BI = -BI / 1.0e5
	
	return BI





def flambda_to_fnu (spec_array, nu_array, lambda_array):

	'''
	converts a spectrum array in Flambda form to Fnu
	
	REMEMBER: flambda dlambda = fnu dnu!!
	'''
	
	return_array=[]
	
	dlambda = fabs ( lambda_array[1] - lambda_array[0])
	dnu = fabs ( nu_array[1] - nu_array[0])

	return_array.append(spec_array[0] * ( dlambda / dnu ))
	for i in range ( 1, len (spec_array) ):
		
		dlambda = fabs ( lambda_array[i] - lambda_array[i-1])
		dnu = fabs ( nu_array[i] - nu_array[i-1])
		
		fnu = spec_array[i] * ( dlambda / dnu )
		
		return_array.append(fnu)
		
	return_array = np.array(return_array)
	
	return return_array
	
	
	
	







	
		
		
	
	
	 
