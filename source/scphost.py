


'''

usage 
	scphost.py put/get host file1 file2
'''
## now copy the nightly regression pdf to online
## this is hosted on the astroaips machine
import pexpect
import sys

Folder = False

for i in range(len(sys.argv)):
	if sys.argv[i]=='help':
		print 'Usage: put/get host path/to/file1 path/to/file2'
		sys.exit()
	if sys.argv[i]=='-r':
		Folder = True	


file1 = sys.argv[3]
file2 = sys.argv[4]
hostname = sys.argv[2]

if Folder: 
	scp = "scp -r -oPubKeyAuthentication=no"
else:
	scp= "scp -oPubKeyAuthentication=no"

if hostname=='iridis':
	USER = "jm8g08"
	HOST = "iridis3_c.soton.ac.uk"
	PASS = "111Neverlose"
	HOME = "/home/jm8g08/"
	
if hostname=='aips':
	USER = "jm8g08"
	HOST = "152.78.192.83"
	PASS = "11Neverlose"
	HOME = "/home/jm8g08/"

if sys.argv[1]=='put':
	FILE = file1
	REMOTE_FILE = HOME + file2
	COMMAND = "%s %s %s@%s:%s" % (scp, FILE, USER, HOST, REMOTE_FILE)

if sys.argv[1]=='get':
	FILE = file2
	REMOTE_FILE = HOME + file1
	COMMAND = "%s %s@%s:%s %s" % (scp, USER, HOST, REMOTE_FILE, FILE)


print COMMAND
child = pexpect.spawn(COMMAND)
child.expect('password:')
child.sendline(PASS)
child.expect(pexpect.EOF)
