import transmissionrpc

server = 'Your IP'
print 'Connecting to: '+server
tr = transmissionrpc.Client(server, port=9091, user='your-user', password='your-passwd')
print 'Connected to: '+server
magnet = raw_input('Insert magnet link: ')
tr.add_uri(magnet)