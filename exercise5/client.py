# Filename:
#      client.py
#Description
# client py which sends a request to the server
# San Andres Deric , BS-IT 2ND
#Honor Code which states the following: I have not given nor received any unathorized help in completing this
#exercise. I am also well aware of the policies stipulated in the AdNU student handbook.


import sys
import socket


if len(sys.argv) < 3:
    print("Usage: {} hostname port_no".format(sys.argv[0]))
    exit(1) 

server = sys.argv[1]
port_no = int(sys.argv[2])

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish a connection to server
sock.connect((server, port_no))

# Communicate
while(True):

    send_data = input("< ")
    sock.send(send_data.encode("utf-8"))

    if send_data == "BYE":
        break

    recv_data = sock.recv(1024)
    print("{}".format(recv_data.decode("utf-8")))

# Close connection
sock.close()