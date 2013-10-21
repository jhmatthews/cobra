#! /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python
'''
	University of Southampton -- JM -- 30 September 2013

				SKINNY

Synopsis:
	Skinny is the front end for the thin shell mode in the
	Python radiative transfer code.	So it's using Python, to run
	PYTHON...confusing, huh!?

Code History:
131008	JM	Initial coding begun. Skinny prints a menu to screen.
'''

# import standard python modules
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import sys, os, subprocess

#import own modules
import read_output as rd
from constants import *
from sub_report import *
import cobra_sub as cobra
import skinny_sub as sub


#sub.print_big_skinny()


print '''
Hello, and welcome to skinny, the frontend for the thinshell model
for the radiative transfer code. What would you like to do?
	0 - run single thin shell model
	1 - run multiple thin shell models
	'''






