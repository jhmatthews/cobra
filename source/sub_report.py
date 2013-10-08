
############################################################	
#					sub_report.py
#
# sub_report is a subroutine which contains functions to deal 
# with reporting on the nightly regression tests for Python
#
############################################################

import os

def Error_warning(string):
	print 'Error: '+string

def Error(string):
	print 'Error: '+string
	sys.exit()


'''
copy_regression_report()
	This copies the a file to the web folder	
	http://www.astro.soton.ac.uk/~jm8g08/python/
'''



def copy_file_to_web(filename):

	## now copy the nightly regression pdf to online
	## this is hosted on the astroaips machine
	import pexpect
	FILE = filename
	REMOTE_FILE = "/home/jm8g08/public_html/pythonrt/regression/"
	USER = "jm8g08"
	HOST = "152.78.192.83"
	PASS = "11Neverlose"
	COMMAND = "scp -oPubKeyAuthentication=no %s %s@%s:%s" % (FILE, USER, HOST, REMOTE_FILE)

	child = pexpect.spawn(COMMAND)
	child.expect('password:')
	child.sendline(PASS)
	child.expect(pexpect.EOF)



'''
send_failure_email()
	if the test fails this sends advising the user
'''
def send_failure_email():
	import smtplib, datetime

	sender = 'jm8g08@soton.ac.uk'
	receiver = 'jm8g08@soton.ac.uk'

	message = """From: Python Test <jm8g08@soton.ac.uk>
	To: James <jimim@hotmail.co.uk>
	Subject: Python Failure

	Python's nightly test of the dev branch failed. 
	Please check http://www.astro.soton.ac.uk/~jm8g08/nightly_regression.pdf
	for the produced latex document.
	"""

	now = datetime.datetime.now()
	time_message = "\nThe time of the test was:" + str(now) + "\n" 
	message = message + time_message
	
	## username and password for sending email
	## should probably make this a python specific email
	username = 'jm8g08'
	password = '111Neverlose'

	## accesss smtp server and send email
	server = smtplib.SMTP('smtp.soton.ac.uk:587')
	server.ehlo()
	server.starttls()	
	server.login(username,password)
	server.sendmail(sender, receivers, message)    
	server.quit()   


'''
check_logfile_length ()
	this function simply executes a series of commands in a row
	the commands are passed to the function as an array
'''

def check_file_length (filename, n):
	print 'have not written yet!'	




#send_failure_email()








