#!/usr/bin/python3
# This is simply working off of 'portscan1.py'
# Very simple, basic portscan
# ===========================
import socket  # Access to functions in the socket library.
#
# termcolor was a package that needed to be installed in preferences.
# This will let us print closed ports in red, and open ports in green.
from termcolor import colored
# -------------------------------

"""Create the socket object
sock = 
) socket.AF_INET        - implies we will/can connect to an IPv4 host.
) socket.SOCK_STREAM    - implies we will be using TCP 3-way handshake packets, not UDP

Remember here we have to use
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)  # Set timeout to 2 seconds. To prevent hangup on single port
# ----------------------------------------

# Function
def portscanner(host, port):
    # ....connect_ex(  looks to see if the connect returns an error, i.e. no connection.
    if sock.connect_ex((host, port)):  # Connect to host, on this port.
        print(colored(f'Port {port} is closed.', "red"))    # Ex:   Port 80 is closed.   (in red text)
    else:
        print(colored(f'Port {port} is open.', "green"))    # Ex:   Port 80 is open.   (in green text)
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------

# method in function
# sock.connect_ex       requires a (string + int)
host = str(input("Please enter an IPv4: "))
port = int(input("Please enter a port: "))
#
portscanner(host, port)  # 10.0.0.114 = local Macbook
print(colored("------------------------", "blue"))
# -----------------------------------------------------------
# Simple scan through the first 1000 ports
for port in range(1, 1000):
    portscanner(host, port)
