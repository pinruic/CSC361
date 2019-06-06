import socket   #for sockets
import sys  #for exit
from time import time 
from datetime import datetime
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = sys.argv[1]
port = int(sys.argv[2])
counter = 1
 
while (counter <= 10):
	msg = "ping"
	s.settimeout(1)
	try:
		a = datetime.now()
		s.sendto(msg, (host, port))
		reply, server_addr = s.recvfrom(1024)
		b = datetime.now()
		rtt = b - a
		print "ping", counter, rtt
	except socket.timeout:
		print 'Request timed out.'

	counter += 1

