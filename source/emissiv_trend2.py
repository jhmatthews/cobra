#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
....University of Southampton -- JM -- 30 September 2013

................plot_emissiv.py 

Synopsis:
....Plot macro atom level emissivities and other information from
....diag file

Usage:
....

Arguments:
'''

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import sys
import os
import subprocess
import read_output as rd
from constants import *

t_init = 8000.0  # this is the temperatrue of the blackbody
imax = 20  # maximum steps we iterate over
i_temp_steps = 500  # step widths in temp space
MACRO = 7	# hardwire macro atom mode

# now we want a list of pywind cmds
# we want to make files
# we want electron density
# we want neutral hydrogen density and non neutral
# pywindcmds = [ 1, 'n', 't',  'i', 1, 1, 1, 1, 2, 0, 'q']

pywindcmds = [
    1,
    'n',
    't',
    'i',
    1,
    1,
    1,
    0,
    'q',
    ]

# first write these commands to a file

inp = open('input_comms', 'w')

for command in pywindcmds:
    inp.write('%s\n' % str(command))
inp.close()

rd.setpars()  # set standard plotting parameters, e.g. tex

# set the band you want to plot emissivities over
# 3000-7000 will get the balmer continuum

wavemin = 3000.0
wavemax = 7000.0

# we read from a template file template.pf

print 'Reading template parameter file'
(keywords, values) = np.loadtxt('template.pf', dtype='string',
                                unpack=True)

# we read a number of arguments from the command line
# the user can decide to change certain keywords

for i in range(len(sys.argv)):
    keyword = sys.argv[i]
    np.where(keywords == 'Line_transfer()'
    for j in range(len(keywords)):
        if keywords[j] == keyword:
            old_value = values[j]
            new_value = sys.argv[i + 1]
            print 'Changing keyword %s from %s to %s' % (keyword,
                    old_value, new_value)

# get the line transfer mode so we know whether to get
mode = int (values[np.where(keywords == 'Line_transfer()')][0]) 
print mode[0]

if mode == MACRO: print 'Using macro atom line transfer'

print mode

# empty arrays to append to

hbeta_list = []
matom_emissivities = []
kpkt_emissivities = []
nh_list = []
h1_list = []
ne_list = []
t_e_list = []
hbeta_quantity = []
halpha_over = []
t_bb = []

mass_loss = float(sys.argv[2]) * 1.0e-19
print 'Mass loss rate is ', mass_loss

# now do the loop over temperature

for i in range(imax):

      # obtain temperature of the star, what we ar eiterating on

    tstar = t_init + i * i_temp_steps

    # print some info for the user

    print 'Starting cycle ' + str(i + 1) + ' of ' + str(imax)
    print 'tstar = %lf' % tstar

    # now we open a file for temporary pf, and write to it

    inp = open('input.pf', 'w')

    # cycle through keywords and write to file

    for j in range(len(keywords)):

        # if the keyword is tstar then we are iterating over it

        if keywords[j] == 'tstar':
            inp.write("tstar		%lf\n" % tstar)
        else:

        # if not just write the value stored in the values array

            inp.write('%s    %s\n' % (keywords[j], values[j]))



    # close file

    inp.close()




    # pf file created, let's run it using latest vers

    os.system('py76c_dev input > output')



    # run py_wind

    os.system('py_wind input < input_comms > pywindout')




    # now get the key values from the pywind files

    root = 'input'

    h1 = rd.thinshell_read(root + '.ioncH1.dat')
    ne = rd.thinshell_read(root + '.ne.dat')
    t_e = rd.thinshell_read(root + '.te.dat')


    rootfolder = 'diag_input/'


    convergence = rd.read_convergence(rootfolder + root)
  
    print '\nconvergence fraction = %f' % convergence

    # now append some important values to array
    # we only want to append if the model has converged!

    if mode == MACRO and convergence == 1.0:
        (matom_emiss, kpkt_emiss) = rd.read_emissivity(rootfolder
                + root)
        hbeta = matom_emiss[3]
        nlevels_macro = len(matom_emiss)
        n_array = np.arange(nlevels_macro)
        hbeta_list.append(hbeta)
        hbeta_quantity.append(PI * hbeta / (2.3e23 * ne ** 2))
        halpha_over.append(matom_emiss[2] / hbeta)
        matom_emissivities.append(matom_emiss)
        kpkt_emissivities.append(kpkt_emiss)

    if convergence == 1.0:
        h1_list.append(h1)
        ne_list.append(ne)
        t_e_list.append(t_e)
        t_bb.append(tstar)

    if mode == MACRO and convergence == 1.0:
        print '\nt_E %8.4e ne %8.4e hbeta %8.4e 4pi j /ne^2 %8.4e h1 %8.4e' \
            % (t_e, ne, hbeta, 4.0 * PI * hbeta / (2.3e23 * ne ** 2),
               h1)

    print '\nt_E %8.4e ne %8.4e' % (t_e, ne)

# we need to normalise hbeta to be in units of erg cm^-3 s-1

hbeta_list = np.array(hbeta_list)
halpha_over = np.array(halpha_over)
ne_list = np.array(ne_list)
t_e_list = np.array(t_e_list)
h1_list = np.array(h1_list)

fig = plt.figure()

# order of things to plot
# t_bb = np.arange(t_init, t_init + (imax)*i_temp_steps, i_temp_steps)# this is the temperatrue of the blackbody

# pi_hbeta_over_nenep = ( 4.0*PI*hbeta_list / ne_list**2  ) / 1.3e+23

# arrays of the predicted values from Osterbrock

# first the array of temperatures Osterbrock gives

t_e_oster = np.arange(2500, 12500, 2500)

# now line intensities

oster_h_beta_absolute = np.array([2.7e-25, 1.54e-25, 8.30e-26,
                                 4.21e-26])  # 4pi j_hbeta / ne **2 values
oster_h_alpha_relative = np.array([3.42, 3.10, 2.86, 2.69])  # ratios of halpha to hbeta from osterbrock
oster_h_gamma_relative = np.array([0.439, 0.458, 0.470, 0.485])  # ratios of hgamma to hbeta from osterbrock
oster_h_delta_relative = np.array([0.237, 0.25, 0.262, 0.271])  # ratios of hdelta to hbeta from osterbrock

# if we are in macro mode we want to plot lots of things

if mode == MACRO:
    plot_list = [halpha_over, hbeta_quantity, hbeta_list, t_bb]
    oster_list = [oster_h_beta_absolute, oster_h_gamma_relative,
                  oster_h_delta_relative]
    ylabel = [r'$H \alpha / H \beta$', r'$4\pi j_{H \beta} / n_e^2$',
              r'$H \beta$', '$T_{bb}$']
else:
    plot_list = [ne_list, t_bb]
    ylabel = ['$n_e$', '$T_{bb}$']

print t_e_list, plot_list[0]

# number of things to plot

n = len(plot_list)

for i in range(n):

    ax = fig.add_subplot(n / 2, 2, i + 1)

    print i
    ax.plot(t_e_list, plot_list[i])
    if i == 0:
        ax.scatter(t_e_oster, oster_h_alpha_relative)
    if i == 1:
        ax.scatter(t_e_oster, oster_h_beta_absolute)
    ax.set_ylabel(ylabel[i])

    ax.set_xlabel('Electron Temp')

# finally, save the figures....

if mode == MACRO:
    plt.savefig('macro.png')
else:
    plt.savefig('nonmacro.png')

