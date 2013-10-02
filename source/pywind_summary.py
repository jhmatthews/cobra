#!/usr/bin/env python -i
import csv, sys, os, array, warnings, subprocess
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pywind_sub as ps

#plt.rcParams[set_autoscale_on]='False'

fname=sys.argv[1]
vers=''
string='~/Documents/Analysis_Scripts/pywindcmds'
if len(sys.argv)>2: 
	if sys.argv[2]!='x':
		print 'Running py_wind...'
		string='~/Documents/Analysis_Scripts/pywindcmds'
		cmdline='py_wind'+vers+' '+fname+' < '+string+vers
		subprocess.check_call(cmdline,shell=True)	

x=[]
z=[]
x1=[]
z1=[]
lx=[]
lz=[]
lx1=[]
lz1=[]

data=[]
IPtemp=[]
tetemp=[]
nhtemp=[]
xtemp=[]
ztemp=[]

tetemp=[]
trtemp=[]

convtemp=[]

vx=[]
vz=[]

H1=[]
H2=[]
C4temp=[]
Si4temp=[]
N5temp=[]
O6temp=[]



ix,iz,x,z,lx,lz,xmax,zmax=ps.get_wind_geom(fname+'.ioncH1.dat')



H1=ps.pywind_read(fname+'.ioncH1.dat',ix,iz)
H2=ps.pywind_read(fname+'.ioncH2.dat',ix,iz)

H=np.empty([iz,ix])
for i in range(iz):
	for j in range(ix):
		H[i][j]=np.log10(H1[i][j]+H2[i][j])



IP=ps.pywind_read(fname+'.IP.dat',ix,iz)
te=ps.pywind_log_read(fname+'.te.dat',ix,iz)
tr=ps.pywind_log_read(fname+'.tr.dat',ix,iz)
vx=ps.pywind_read(fname+'.vx.dat',ix,iz)
vz=ps.pywind_read(fname+'.vz.dat',ix,iz)
nagn=ps.pywind_log_read(fname+'.nphot.dat',ix,iz)
ne=ps.pywind_log_read(fname+'.ne.dat',ix,iz)
ll=ps.pywind_log_read(fname+'.line_lum.dat',ix,iz)
lt=ps.pywind_log_read(fname+'.tot_lum.dat',ix,iz)




vxz=np.empty([iz,ix])
for i in range(iz):
	for j in range(ix):
		vxz[i][j]=np.log10(np.sqrt(vx[i][j]*vx[i][j]+vz[i][j]*vz[i][j]))


#These are the lines for reading in all the extra ions fractions

C3=ps.pywind_log_read(fname+'.ionC3.dat',ix,iz)
C4=ps.pywind_log_read(fname+'.ionC4.dat',ix,iz)
C5=ps.pywind_log_read(fname+'.ionC5.dat',ix,iz)
C6=ps.pywind_log_read(fname+'.ionC6.dat',ix,iz)
C7=ps.pywind_log_read(fname+'.ionC7.dat',ix,iz)
Si4=ps.pywind_log_read(fname+'.ionSi4.dat',ix,iz)
N5=ps.pywind_log_read(fname+'.ionN5.dat',ix,iz)
O6=ps.pywind_log_read(fname+'.ionO6.dat',ix,iz)

if len(sys.argv)>2: 
	if sys.argv[2]!='x':
		cmdline='py_wind '+fname+' < ~/Documents/Analysis_Scripts/pywindcmds2'
		subprocess.check_call(cmdline,shell=True)
ndisk=ps.pywind_log_read(fname+'.nphot.dat',ix,iz)
tauc4=ps.pywind_read(fname+'.ionC4.dat',ix,iz)


lwind_scale=[lx[1]-1,lx[len(lx)-1],lz[1]-1,lz[len(lz)-1]]
wind_scale=[1e13,1e18,1e13,1e18]

fig=plt.figure(figsize=(8.3,11.7),dpi=80)
fig.suptitle(fname,fontsize=24,fontweight='bold')
fig.subplots_adjust(hspace=0.3,wspace=0.2)
plt.rcParams['font.size']=8

ax=fig.add_subplot(4,2,1)
ax.set_autoscale_on(False)
ax.set_title('log Hydrogen Density',fontsize=12)
plt.axis(lwind_scale)
plt.contourf(lx,lz,H,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
plt.colorbar()

ax=fig.add_subplot(4,2,3)
ax.set_autoscale_on(False)
ax.set_title('log Streamline velocity',fontsize=12)
plt.axis(lwind_scale)
plt.contourf(lx,lz,vxz,[5,6,7,8,9,10])
plt.colorbar()

ax=fig.add_subplot(4,2,5)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log Electron Temperature',fontsize=12)
plt.contourf(lx,lz,te,[3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7])
plt.colorbar()

ax=fig.add_subplot(4,2,7)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('Radiation temperature',fontsize=12)
plt.contourf(lx,lz,tr,[3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7])
plt.colorbar()

ax=fig.add_subplot(4,2,2)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log Ionization parameter',fontsize=12)
plt.contourf(lx,lz,IP,[-4,-3,-2,-1,0,1,2,3,4,5,6,7])
plt.colorbar()

ax=fig.add_subplot(4,2,4)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log Line luminosity',fontsize=12)
plt.contourf(lx,lz,ll,np.arange(30,44,2))
#ax.set_title('log Number of AGN photons',fontsize=12)
#plt.contourf(lx,lz,nagn,[0,1,2,3,4,5,6])
plt.colorbar()

ax=fig.add_subplot(4,2,6)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
#ax.set_title('log Number of disk photons',fontsize=12)
#plt.contourf(lx,lz,ndisk,[0,1,2,3,4,5,6,7,8,9,10])
ax.set_title('log tot luminosity',fontsize=12)
plt.contourf(lx,lz,lt,np.arange(30,44,2))
plt.colorbar()

ax=fig.add_subplot(4,2,8)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log n_e',fontsize=12)
plt.contourf(lx,lz,ne,np.arange(0,15,1))
#plt.contourf(lx,lz,ne,np.arange(np.min(ne),np.max(ne),2))
plt.colorbar()


plt.savefig(fname+'geometry.jpg',dpi=80,facecolor='w',edgecolor='w',orientation='portrait')
os.system('open -a preview '+fname+'geometry.jpg')

print np.max(ne),np.min(ne), ne


fig=plt.figure(figsize=(8.3,11.7),dpi=80)
fig.suptitle(fname,fontsize=24,fontweight='bold')
fig.subplots_adjust(hspace=0.3,wspace=0.2)
plt.rcParams['font.size']=8

cont=[-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

ax=fig.add_subplot(4,2,1)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log CIII proportion',fontsize=12)
plt.contourf(lx,lz,C3,cont)
plt.colorbar()

ax=fig.add_subplot(4,2,3)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log CIV proportion',fontsize=12)
plt.contourf(lx,lz,C4,cont)
plt.colorbar()

ax=fig.add_subplot(4,2,5)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log CV proportion',fontsize=12)
plt.contourf(lx,lz,C5,cont)
plt.colorbar()

ax=fig.add_subplot(4,2,7)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log CVI proportion',fontsize=12)
plt.contourf(lx,lz,C6,cont)
plt.colorbar()

ax=fig.add_subplot(4,2,4)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log SiIV proportion',fontsize=12)
plt.contourf(lx,lz,Si4,cont)
plt.colorbar()

ax=fig.add_subplot(4,2,6)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log NV proportion',fontsize=12)
plt.contourf(lx,lz,N5,cont)
plt.colorbar()

ax=fig.add_subplot(4,2,8)
ax.set_autoscale_on(False)
plt.axis(lwind_scale)
ax.set_title('log OVI proportion',fontsize=12)
plt.contourf(lx,lz,O6,cont)
plt.colorbar()


plt.savefig(fname+'ions.jpg',dpi=80,facecolor='w',edgecolor='w',orientation='portrait')


