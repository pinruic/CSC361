import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	sys.exit()

s.connect((sys.argv[1], int(sys.argv[2])))

try:
	s.send("GET /" + sys.argv[3] + " HTTP/1.1\r\n\r\n")
except socket.error:
	sys.exit()

reply = s.recv(1024)
print reply

s.close()

