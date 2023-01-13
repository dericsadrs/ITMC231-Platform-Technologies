# Filename:
#      server.py
#
# Descrition:
#      This program is used in tandem with client.py
#      This demonstrates the use of sockets to create a TCP server.
#
# Author:
#      Glenn G. Fabia
#      gfabia@gbox.adnu.edu.ph
#      Ateneo de Naga University
#
# Notes:
#      This is a handout for ITMC231 - Platform Technologies
#      Intersession S/Y 2020-2021

import sys
import socket

if len(sys.argv) < 2:
    print("Usage: {} port_no".format(sys.argv[0]))
    exit(1) 

port_no = int(sys.argv[1])

print("Server starting ...");
# Create a socket for incoming connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a port
sock.bind(('localhost', port_no))

# Mark the socket so it will listen for incoming connections
sock.listen(5)
print("Server listening to port {} ...".format(port_no))
print("Waiting for connection(s) ...");

# Accept new connection
(conn, addr) = sock.accept()
print("Client succesfully connected ...")

# Communicate
(recv_data, temp) = conn.recvfrom(1024)
print("Message received from client :", recv_data.decode())

print("Sending reply ...")
send_data = "I got your message!"
conn.sendto(send_data.encode("utf-8"), addr)

# Close connection
print("Closing connection ...")
conn.close()