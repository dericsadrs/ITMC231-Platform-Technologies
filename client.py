# Filename:
#      client.py
#
# Descrition:
#      This program is used in tandem with server.py
#      This demonstrates the use of sockets to create a TCP client.
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

if len(sys.argv) < 3:
    print("Usage: {} hostname port_no".format(sys.argv[0]))
    exit(1) 

server = sys.argv[1]
port_no = int(sys.argv[2])

print("Client starting ...")
# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to server '{}' at port {} ...".format(server, port_no))
# Establish a connection to server
sock.connect((server, port_no))

print("Connection successful!")

# Communicate

send_data = input("Please type a message : ")

print("Sending message to server ...")
sock.send(send_data.encode("utf-8"))

print("Message sent! Awaiting reply ...")
recv_data = sock.recv(1024)

print("Server says :", recv_data.decode("utf-8"))

# Close connection
sock.close()