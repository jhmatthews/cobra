#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
	critical_density.py

This program calculates critical densities for ions

'''



import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
import os, sys
from constants import *
import classes as cls

#print ECS_CONSTANT



def q12(line, T):

	'''calculate q12 for a line at temperature T'''

	term_a = 1.0*line.g_u / line.g_l
	term_b = q21(line, T)
	term_c = np.exp ( H_OVER_K * line.freq / T )

	return term_a * term_b * term_c 



def q21(line, T):

	'''calculate q21 for a line at temperature T'''

	term_a = 1.0*line.g_l / line.g_u
	term_b = line.osc / (line.freq * np.sqrt(T) )
	term_c = ECS_CONSTANT * 8.629e-9

	return term_a * term_b * term_c 



def A21(line):
	
	'''calculate A21 for a given line'''

	term_a = (line.freq**2) * line.osc
	term_b = (1.0*line.g_l) / (1.0*line.g_u)
	term_c = A21_CONSTANT

	return term_a * term_b * term_c 



def read_line_info(filename):

	line_array_read = np.loadtxt(filename, comments='#', unpack = True, dtype = 'string')
	
	line_array_read = np.transpose(line_array_read)
	
	print line_array_read[0]

	line = np.ndarray( len(line_array_read),dtype=np.object)
	
	for i in range(len(line)):
		z = float (line_array_read[i][1])
		ion = float (line_array_read[i][2])
		wave = ANGSTROM * float (line_array_read[i][3])
		freq = C / ( wave ) 
		osc = float (line_array_read[i][4])
		gl = int (line_array_read[i][5])
		gu = int (line_array_read[i][6])
		ll =  int (line_array_read[i][9])
		lu =  int (line_array_read[i][10])
		
		line[i] = cls.line(z, ion, wave, freq, osc, gl, gu, ll, lu)
		
	#line = cls.line(0,0,0,0,0)
	return line


l = read_line_info ("data/atomic_macro/h20_lines.py")

nentries = len(l)


# wavelengths we want without decimals.
# for the moment this is just Paschen alpha and Halpha
reference_array = [6562, 18750]
#reference_array = [2876109]



# now we want to put the values associated with the lines into 
n=0
store = np.ndarray( len(l),dtype=np.object)

for i in range(nentries):

	for j in range(len(reference_array)):

		if int(l[i].wavelength) == reference_array[j]: 
			store[n] = l[i]
			n+=1


T=10000.0	# 10000K

#print q12(l[19], T)

# n is number of lines we want to look at 
for i in range(n):
	i_lev = store[i].lu
	qsum = 0	# sum of q coefficients
	Asum = 0	# sum of A coefficients
	for j in range(len(l)):
		if l[j].lu == i_lev:
			print A21(l[j])
			print 'j < i: ', l[j].lu, l[j].ll, i_lev
			qsum += q21(l[j], T)
			Asum += A21(l[j])

		if l[j].ll == i_lev and l[j].ll<5:
			print 'j != i: ', l[j].ll, l[j].lu, i_lev
			term = q12(l[j], T)
			qsum += q12(l[j], T)

	crit_density = Asum / qsum

	print "For wavelength %f critical density is %8.4e" % (store[i].wavelength, crit_density)
	

















	
