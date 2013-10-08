########################################################################
#
#	University of Southampton, 130703
#
#	standard_tests: "makelatex.py"
#		
#	Makes latex output of figures and compiles as single PDF w/ captions.
#	This output serves as a document of regression testing and should be
#	backed up on Dropbox or similar public area
#
#########################################################################

#import modules to use
import numpy as np
import os, sys

#version number is given by pytest bash script
version=sys.argv[1]

#make sure you run this script from the testing directory!
current_dir = os.getcwd()

#create latex file
latex_file=open('figures_test_'+version+'.tex', 'w')

#strings for starting and ending document
header_string=r'''\documentclass{article}
\usepackage{graphicx}
\begin{document}
'''

title_string=r'\title{Regression Test for Python '+version+'}\n\n'+'\maketitle\n\n'

first_page_string=r'''

This documents a regression test conducted on the date shown for the version 
of the code shown in the title. The filenames are as follows

\begin{itemize}
\item svtest\_1- standard SV model with Lucy/Mazzali ionization scheme.
\item svtest\_2- standard SV model with Lucy/Mazzali ionization scheme.
\item run110e- The fiducial AGN model from Higginbottom et al. 2013.
\item 1d\_sn- A 1 dimensional supernova model.
\end{itemize}

A number of comparison plots are documented here.
\newpage


'''

footer_string=r'''\end{document}'''

#write header to tex file
latex_file.write(header_string+'\n\n'+title_string)
latex_file.write(first_page_string)

# suite is an array of the files that we want to test
suite = ['svtest_1', 'svtest_2', 'run110e', '1d_sn']


figures = np.array(['run110e_compsummary.jpg', 'run110e_compsources.jpg', 'svtest_1_compsummary.jpg', 'svtest_1_compsources.jpg',  '1d_snspectrum_summary.jpg', '1d_snspectrum_sources.jpg', '1d_sn.spec_summary.jpg', 'fig5.png', 'fig5_paper.png'])


outputs = ['/Users/jmatthews/Documents/nightly_test/outputs/'+fig for fig in figures]
templates = ['/Users/jmatthews/Documents/nightly_test/templates/'+fig for fig in figures]
#plots = ['/Users/jmatthews/Documents/nightly_test/plots/'+fig for fig in figures]
plots=[]

os.system("ls /Users/jmatthews/Documents/nightly_test/plots/*jpg > templistfile")

tempfile_toread  = open('templistfile', 'r')
for line in tempfile_toread:
	data=line.split()
	plots.append(data[0])

if len(outputs)!=len(templates):
	print 'Errror when plotting: different numbers of outputs and templates, exiting'
	

#create figures and captions
for i in range(len(plots)):
	latex_file.write(r'\begin{figure}'+'\n\centering\n')
	latex_file.write(r'\includegraphics[width=1.4\textwidth]{'+plots[i]+'}\n')
	latex_file.write(r'\caption{}'+'\n\n')
	latex_file.write(r'\end{figure}'+'\n\n')

	#put template below it for comparison
	#latex_file.write(r'\begin{figure}'+'\n\centering\n')
	#latex_file.write(r'\includegraphics[width=1.0\textwidth]{'+templates[i]+'}\n')
	#latex_file.write(r'\caption{Filename:}'+'\n\n')
	#latex_file.write(r'\end{figure}'+'\n\n')


#write end document and close file
latex_file.write(footer_string)
latex_file.close()

#compile latex
os.system('pdflatex figures_test_'+version)

os.system('mv figures_test_'+version+'.pdf /Users/jmatthews/Documents/nightly_test/tests/')
os.system('mv figures_test_'+version+'.tex /Users/jmatthews/Documents/nightly_test/tests/')
os.system('mkdir /Users/jmatthews/Documents/nightly_test/plots/plots_'+version+'; mv /Users/jmatthews/Documents/nightly_test/plots/*jpg  /Users/jmatthews/Documents/nightly_test/plots/plots_'+version+'/')
os.system('rm -f *.aux *.log templistfile')
#All done.




