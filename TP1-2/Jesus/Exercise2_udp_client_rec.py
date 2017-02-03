import socket
import sys

address = ('localhost', 1212)

if (len(sys.argv) == 3):
    address = (sys.argv[1], int(sys.argv[2]))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # TCP
sock.sendto('', address)
# Get KeyboardInterrupt to close the socket
try:
    while (True):
        data = sock.recv(1024)
        if (data == chr(26)):
            break
        print data
except KeyboardInterrupt:
    # chr(26) is EOF in ASCII
    sock.sendto(chr(26), address)
    sock.close()
    print
