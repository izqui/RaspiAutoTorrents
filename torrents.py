import transmissionrpc
import base64
from os import listdir
from os import remove
from os.path import isfile, join


server = 'Your IP'
print 'Connecting to: '+server
tr = transmissionrpc.Client(server, port=9091, user='your-user', password='your-passwd')
print 'Connected to: '+server


mypath = '/Users/izqui97/Torrents'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]




for f in onlyfiles:
	if '.torrent' in f:
		
		b = base64.b64encode(open(f, 'r').read())
		print 'Sending '+f
		added = tr.add(b)
		if added:	
			remove(f)	
			
			


