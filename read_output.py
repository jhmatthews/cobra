'''
	University of Southampton -- JM -- 30 September 2013

				read_output.py

Synopsis:
	this enables one to read outputs from the Python radiative transfer code

Usage:
	

Arguments:
'''

# we need the classes and numpy modules 
import classes as cls
import numpy as np
import matplotlib.pyplot as plt


def read_spec_file (filename):
    
    '''reads a Python .spec file and places in specclass array,
       which is returned'''
    
    if not '.spec' in filename: 
        filename = filename + '.spec'
        
    
    # initialise the spectrum array with blank arrays
    spectrum = cls.specclass ([],[],[],[],[],[], [], [], []) 
    
    # first read the file into a temporary storage array
    spectrum_temp = np.loadtxt (filename, comments ='#', unpack=True)
    
    # now set the correct elements of the class to be the temporary array
    spectrum.freq = spectrum_temp[0]
    spectrum.wavelength = spectrum_temp[1]
    spectrum.emitted = spectrum_temp[2]
    spectrum.censrc = spectrum_temp[3]
    spectrum.disk = spectrum_temp[4]
    spectrum.wind = spectrum_temp[5] 
    spectrum.scattered = spectrum_temp[6]
    spectrum.hitsurf = spectrum_temp[7]
    spectrum.spec = spectrum_temp[8:]
        
     #finally, return the spectrum class which is a series of named arrays      
    return spectrum



def read_spectot_file (filename):
    
    '''reads a Python .spec_tot file and places in spectotclass array,
       which is returned'''
    
    if not '.spec_tot' in filename: 
        filename = filename + '.spec_tot'
        
    
    # initialise the spectrum array with blank arrays
    spectrum = cls.spectotclass ([],[],[],[],[],[], [], []) 
    
    # first read the file into a temporary storage array
    spectrum_temp = np.loadtxt (filename, comments ='#', unpack=True)
    
    # now set the correct elements of the class to be the temporary array
    spectrum.freq = spectrum_temp[0]
    spectrum.wavelength = spectrum_temp[1]
    spectrum.emitted = spectrum_temp[2]
    spectrum.censrc = spectrum_temp[3]
    spectrum.disk = spectrum_temp[4]
    spectrum.wind = spectrum_temp[5] 
    spectrum.scattered = spectrum_temp[6]
    spectrum.hitsurf = spectrum_temp[7]
    
    #finally, return the spectrum class which is a series of named arrays    
    return spectrum



#Reading arguments from command line

def read_args( sysargv ):
    
	'''This function reads arguments from the command line with various options specified by the user'''
	modea = cls.modeclass(False, False, False, False, False, False, False, False, False, False, False)
    
	stored1 = cls.stored_args(0,0,0,0,0,0,0)
    
	modea.sources = True
    
	if (len(sysargv)<3):
		stored1.ibin=1
        
	for i in range(len(sysargv)):
        
		if sysargv[i]=='-s': 
			modea.sm=True
			stored1.fname_cmd=sysargv[i+1]
            
		if sysargv[i]=='-n': 
			modea.norm=True
            
		if sysargv[i]=='-r': 
			modea.range=True
			stored1.lmin_arg=float(sysargv[i+1])
			stored1.lmax_arg=float(sysargv[i+2])

		if sysargv[i]=='-c':
			modea.comp=True
			try:
				n_to_comp = int(sysargv[i+1])
			except:
				n_to_comp = 1 
		if sysargv[i]=='-nc': 
			modea.norm=True
			modea.comp=True	
            
		if sysargv[i]=='-res': 
			modea.resid=True
            
		if sysargv[i]=='-h' or sysargv[i]=='-h' or sysargv[i]=='help': 
			modea.help=True
            
		if sysargv[i]=='-rel': 
			modea.resid=True
			modea.relative_res=True
            
		if sysargv[i]=='lines': 
			modea.vlines=True
            
		if sysargv[i]=='sources': 
			modea.sources=False
            
		if sysargv[i]=='-log': 
			modea.log=True
			#lmin_log=float(sysargv[i+1])
			#lmax_log=float(sysargv[i+2])
            
		if sysargv[i]=='-max':
			modea.mx=True
			stored1.maximum_y=float(sysargv[i+1])
            
		if sysargv[i]=='-name':
			stored1.filename=sysargv[i+1]
            
		if sysargv[i]=='-title':
			stored1.title=sysargv[i+1]
               
	if modea.comp:
		stored1.filename = sysargv[1:n_to_comp+1]  
	else:           
		stored1.filename = sysargv[1]   
    # return mode and stored arguments to user        
	return modea, stored1





# set some standard parameters
def setpars():
    
	print 'Setting plot parameters for matplotlib.'
	plt.rcParams['lines.linewidth'] = 1.0
	plt.rcParams['axes.linewidth'] = 1.3
	plt.rcParams['font.family'] = 'serif'
	plt.rcParams['font.serif'] = 'Times New Roman'
	plt.rcParams['text.usetex']='True'
    
	return 0








