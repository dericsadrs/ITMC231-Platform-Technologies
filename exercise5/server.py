# Filename:
#      server.py
#
#Filename and Description,
#server.py receives request from client.py
# San Andres Deric , BS-IT 2ND
#Honor Code which states the following: I have not given nor received any unathorized help in completing this
#exercise. I am also well aware of the policies stipulated in the AdNU student handbook.

import os
import sys
import socket

if len(sys.argv) < 2:
    print("Usage: {} port_no".format(sys.argv[0]))
    exit(1) 

port_no = int(sys.argv[1])

# Create a socket for incoming connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a port
sock.bind(('localhost', port_no))

# Mark the socket so it will listen for incoming connections
sock.listen(5)

while True:
    # Accept new connection
    (conn, addr) = sock.accept()
    clientProc = os.fork()
    if clientProc != 0:
        print ("Server PID = {}".format((clientProc)))
        print(" Client {}:{} Sucessfully connected to PID = {} ".format(addr[0],str(addr[1]),clientProc))

    # Communicate
    while True:
        # Receive request
        (recv_data, temp) = conn.recvfrom(1024)
        request = recv_data.decode()
        print("[{}:{}] > {}".format(addr[0],str(addr[1]),request))

        send_data = [min(request.split(",")),max(request.split(",")),"{","}","error: Could not understand request."]
        

        if request == "BYE":
            print("Client {}:{} sucessfully disconnected.".format(addr[0],sys.argv[1]))
            break
        elif any(char.isalpha() for char in request.split(',')):
            conn.sendto("[{}:{}]".format(addr[0],sys.argv[1]).encode("utf-8"), addr)
            conn.sendto(" > {} {} {}".format(send_data[2],send_data[4],send_data[3]).encode("utf-8"),addr)
        else:
            conn.sendto("[{}:{}]".format(addr[0],sys.argv[1]).encode("utf-8"), addr)
            conn.sendto(" > {} pid: {} min: {} max: {} {} ".format(send_data[2], clientProc,send_data[0],send_data[1],send_data[3]).encode("utf-8"),addr)

        

    # Close connection
    print("Closing connection ...")
    conn.close()
