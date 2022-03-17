#!/usr/bin/python3

# Very simple, basic portscan
# Execute:      # python3 portscan1.py
# ===========================

import socket  # Access to functions in the socket library.

"""Create the socket object
) socket.AF_INET        - implies we will/can connect to an IPv4 host.
) socket.SOCK_STREAM    - implies we will be using TCP 3-way handshake packets, not UDP
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ----------------------------------------
# Function
# ...connect_ex(   checks for error if connection is not established.
def portscanner(host, port):
    if sock.connect_ex((host, port)):  # Connect to host, on this port.
        print(f'Port {port} is closed.')
    else:
        print(f'Port {port} is open.')
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------

portscanner("10.0.2.7", 443)  # 10.0.0.114 = local Macbook
# -----------------------------------------------------------
for x in range(1, 1000):
    portscanner("10.0.2.7", x)
