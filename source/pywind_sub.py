
import numpy as np



def get_wind_geom(fname):
	x=[]
	z=[]
	lx=[]
	lz=[]
	xmax=0.0
	zmax=0.0
	inp =open(fname,'r')
	line=inp.readline()
	line=inp.readline()
	for line in inp.readlines():
		temp=line.split()
		print temp
		if temp[0]!='#':
			if int(temp[5])==0:
				x.append(float(temp[0]))
				lx.append(np.log10(float(temp[0])+1))
			if int(temp[4])==0:
				z.append(float(temp[1]))
				lz.append(np.log10(float(temp[1])+1))
			if int(temp[3])>-1:
				xmax=float(temp[0])
				zmax=float(temp[1])
	ix=len(x)
	iz=len(z)
	return (ix,iz,x,z,lx,lz,xmax,zmax)



def pywind_read(fname,x,z):
	array=np.empty([z,x])
	inp =open(fname,'r')
	line=inp.readline()
	line=inp.readline()
	for line in inp.readlines():
		temp=line.split()
		if temp[0]!='#':
			if int(temp[3])>-1:
				array[int(temp[5]),int(temp[4])]=float(temp[2])
			else:
				array[int(temp[5]),int(temp[4])]=-999
	output=np.ma.masked_equal(array,-999)

	return (output)

def pywind_log_read(fname,x,z):
	array=np.empty([z,x])
	inp =open(fname,'r')
	line=inp.readline()
	line=inp.readline()
	for line in inp.readlines():
		temp=line.split()
		if temp[0]!='#':
			if int(temp[3])>-1:
				array[int(temp[5]),int(temp[4])]=np.log10(float(temp[2]))
			else:
				array[int(temp[5]),int(temp[4])]=-999
	output=np.ma.masked_equal(array,-999)

	return (output)


def get_wind_geom58(fname):
	x=[]
	z=[]
	lx=[]
	lz=[]
	xmax=0.0
	zmax=0.0
	inp =open(fname,'r')
	line=inp.readline()
	line=inp.readline()
	for line in inp.readlines():
		temp=line.split()
		if int(temp[5])==0:
			x.append(float(temp[0]))
			lx.append(np.log10(float(temp[0])+1))
		if int(temp[4])==0:
			z.append(float(temp[1]))
			lz.append(np.log10(float(temp[1])+1))
		if int(temp[3])>-1:
			xmax=float(temp[0])
			zmax=float(temp[1])
	ix=len(x)
	iz=len(z)
	return (ix,iz,x,z,lx,lz,xmax,zmax)



