# We are simply gathering a MAC address from a target IP
# The plan in the long term is to arp-spoof
#   but this is just actually to gather the target MAC address.


import scapy.all as scapy

def get_mac(ip):

    # Here, we are creating an ARP request ourselves to ask who has the specific IP we asked for.
    arp_request = scapy.ARP(pdst=ip)

    # Here, we are setting our destination MAC to broadcast MAC address to make sure
    # it is sent to all the clients who are on the same network
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # This variable is your packet that will be sent across the network, as it contains information about MAc and ARP
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    # srp stands for send and receive packet.

    return answered_list[0][1].hwsrc


# In our packet, op is 2 because op=1 means a request whereas we don't want a request.
# What we want is a response for which op=2
# Also in the below line what we have done is crafted a response for the victim saying my machine is the router


# ------------------------------

print(get_mac("10.0.2.15"))
# ------------------------------
