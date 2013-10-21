#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
astro_func.py contains functions for things like eddington fraction and alpha_ox
'''

from constants import *


def alp_ox (L_X, L_O):
	'''
	Calculates alpha ox for a given 2kev and 2500A luminosity	
	'''
	
	alpha = 0.3838 * np.log10( L_X / L_O )
	
	return alpha
	
	
def Ledd (m):
	'''
	calculates eddington luminosity for a mass m
	'''
	
	consts = (4.0 * PI * G * C * MPROT ) / THOMPSON
	
	L = consts * m
	
	return L
	
	

def mdot_from_edd ( edd_frac, m ):
	''' 
	calculates an accretion rate from an eddington fraction
	mass m
	'''
	
	L = Ledd (m)		# eddington luminosity
	
	mdot = L / ( edd_frac * (C ** 2) )
	
	return mdot


def L_two (L_X, alpha):
	'''
	L_two calculates the monochromatic X-ray luminosity at 2Kev
	
	Arguments:
		L_X 		2-10kev luminosity in ergs
		alpha	power law slope of spectrum
	'''
	
	f2 = 2000.0 / HEV	# freq at 2 kev
	f10 = 10000.0 / HEV 	# freq at 10 kev
	
	
	const_agn= L_X / ((( (f10**( alpha + 1.))) -  (f2**( alpha + 1.0))) /(alpha + 1.0))
	
	L = const_agn*f2**alpha

	return L
	
	
	
def L_2500 ( mdot, mbh ):
	'''
	L_two calculates the monochromatic X-ray luminosity at 2Kev
	
	Arguments:
		L_X 		2-10kev luminosity in ergs
		alpha	power law slope of spectrum
	'''
	#spec_disk (f1,f2,m,mdot,rmin,rmax)

	
	return 1.0e30
	
	
def L_bol ( mdot, mbh ):
	
	rmin = 0.5 * Schwarz ( mbh )		# gravitational radius
	rmax = 1.0e17				# standard for models
	
	f1 = 1.0e14; f2 = 1.0e18
	freq, spec = spec_disk (f1,f2,mbh,mdot,rmin,rmax)
	
	df = freq[1] - freq[0]
	sum_spec = df * spec[0]
	
	for i in range(1, len(freq) - 1 ):
		df = freq[i] - freq[i-1]
		sum_spec += df * spec[0]
		
	sum_spec += df * spec[-1]
		
	return sum_spec



def Schwarz(m):
	return 2.0 * G * m / (C**2)


	
def spec_disk (f1,f2,m,mdot,rmin,rmax):
	import pylab
	tref=tdisk(m, mdot, rmin)
	nfreq=(f2/f1)/10
	freq=np.linspace(f1,f2,nfreq)
	spec=np.empty(nfreq)
	dfreq=freq[1]-freq[0]
	rtemp=np.logspace(np.log10(rmin),np.log10(rmax),num=30)
	rdisk=[]
	for j in range(len(rtemp)-1):
		#print j, (len(rtemp)-1)
		rdisk.append((rtemp[j]+rtemp[j+1])/2.0)
		r=rdisk[j]/rmin
		area=PI*(rtemp[j+1]*rtemp[j+1]-rtemp[j]*rtemp[j])
		t=(teff(tref,r))
		print t
		for i in range(len(freq)):
			#print len(freq)
			spec[i]=spec[i]+(planck_nu(t,freq[i])*area*PI*2)
		f = np.array(freq)
		pylab.plot(f, planck_nu(t,f))
		#pylab.plot(freq, spec)
	pylab.show()
	return freq,spec
	
#def summarise ("model.pf")



def tdisk (m, mdot, r):
	t = 3. * G / (8. * PI * STEFAN_BOLTZMANN) * m * mdot / (r * r * r)
  	t = pow (t, 0.25)
  	return (t)

def teff (t, x):
	q = (1.e0 -  (x ** -0.5e0)) / (x * x * x);
      	q = t * (q ** 0.25e0);
	return (q)


def planck_nu (T, nu):
    x = H * nu / (BOLTZMANN * T)
    #print x, nu
    f = (2. * H * nu ** 3.) / (C ** 2. * (np.exp(x) - 1.))
    return f




	
	
	































