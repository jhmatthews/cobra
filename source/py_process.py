#! /Library/Frameworks/Python.framework/Versions/Current/bin/python
'''
	University of Southampton- JM- 22 August 2013

				pytest.py

Synopsis:
	py_process.py is the script which processes the outputs from python's regression
	testing suite

Usage:
	python pytest.py -path [path/to/version] -m [mode] -f [custom_filename for mode 4]

Arguments:

	-m mode
		the mode you want to test
		0- just check compilation (default)
		1- just check python runs (nightly)
		2- standard regression test (weekly)
		3- long regression test (prerelease)
		4- custom set of files

	-path [path/to/version]
		the folder of the version you want to test.
		default is $PYTHON/progs/python_dev/	
'''

## import modules we want to use
import numpy as np
import matplotlib.pyplot as plt
import os, sys, subprocess
from sub_report import *
import pytest_sub as sub
import datetime, subprocess
