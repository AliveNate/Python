import os
import ipaddress
# ==========================================================================================
# =======================================================
# imported ping from stackoverflow comment.
def ping(host):
    # Returns True if host responds to a ping request
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0
# ==========================================================================================
# ========================================================
# The parseIP function is from lab1
def parseIP(cidrNotation):
    addressSplit = cidrNotation.split('/')
# We just split up the primary address from the subnet
    ip = addressSplit[0]
    cidrSubnet = addressSplit[1]
# ipSplit is turning this into an auto list
    # [192][168][10][3]
    ipSplit = ip.split('.')
    return (ipSplit, cidrSubnet)
''' Now we have the address, split into a list and subnet:
ipSplit = [192][168][10][2]
cidrSubnet = 26
   '''
# ==========================================================================================
# ===========================================================
# The convertCidrToDec function is from lab1
def convertCidrToDec(cidrSubnet):
    netmask = ""
    for x in range(0, int(cidrSubnet)):
        netmask += str(1)

    for x in range(0, 32-int(cidrSubnet)):
        netmask += str(0)

    netmask1 = netmask2 = netmask3 = netmask4 = ""
    for x in range(0, 8):
        netmask1 += str(netmask[x])
    for x in range(8, 16):
        netmask2 += str(netmask[x])
    for x in range(16, 24):
        netmask3 += str(netmask[x])
    for x in range(24, 32):
        netmask4 += str(netmask[x])

    netmask1 = str(int(netmask1, base=2))
    netmask2 = str(int(netmask2, base=2))
    netmask3 = str(int(netmask3, base=2))
    netmask4 = str(int(netmask4, base=2))
    return (netmask1, netmask2, netmask3, netmask4)
# ==========================================================================================
# ============================================================
# The printIPsSubnet function is from lab 1
def printIPsInSubnet(ip, netmask):
    if int(netmask[2]) < 255:
        count3 = 255 - int(netmask[2])
        for loop3 in range(0, count3):
            for loop4 in range(1, 256):
                print("{}.{}.{}.{}".format(ip[0], ip[1], loop3, loop4))
    elif int(netmask[3]) < 255:
        count4 = 255 - int(netmask[3])
        for loop4 in range(1, count4):
            print("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], loop4))
            # ==========================================================================================
# ==============================================================

# Test Call
# Line right below is for the internal network.
# This is from the first function, a straight ping.
# Remember that 192.168.10.2 is the home address in Kali
print("\nThe ping = ")
# Original address to ping from lab
print(ping("192.168.10.2"))
print("We just pinged the Kali home network.")

# Worked
print(ping("139.130.4.5"))
print("We just pinged: 139.130.4.5   the largest carrier in Austrailia.")

# Worked
print(ping("8.8.8.8"))
print("We just pinged: 8.8.8.8   ---    google-public-dns-a.google.com   ")

# Worked
print(ping("139.130.4.5"))
print("We just pinged: 139.130.4.5   ---    ns1.telstra.net   ")

print("\n\n")
# ==========================================================================================
# Call the function, we need a host, startport, and endport
# If called from terminal: ./portscanner.py 192.168.10.2 1 100
# We are asking for an IP address, the Kali one here
cidrNotation = input("Enter the network to search ports: e.g. 192.168.10.2/26 \n\t\t\t\t\t\t\t\t")
parseString = parseIP(cidrNotation)
ip = parseString[0]
cidrSubnet = parseString[1]

# We have the ping function at the top, and have split the subs
# Using format, we will use the IP splits to ping.
print(ping("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3])))



# print(ping("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], 3)))
''' Right above, is not the Kali address.
If we are not connected to Win7, we will get:
---------------------------------------------
PING 192.168.10.3 (192.168.10.3) 56(84) bytes of data.
From 192.168.10.2 icmp_seq=1 Destination Host Unreachable

--- 192.168.10.3 ping statistics ---
1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms

False
'''
# ==========================================================================================




# ==========================================================================================
# This is the same for listing as the orginal lab 1
# Now format and produce the list of IP address and we will ping each.
print('\n------------------------')
print('\nNow display the primary address for the whole lab.')
print('IP:{}.{}.{}.{}/{}'.format(ip[0], ip[1], ip[2], ip[3], cidrSubnet))

netmask = convertCidrToDec(cidrSubnet)
print("subnet:{}.{}.{}.{}".format(netmask[0], netmask[1], netmask[2], netmask[3]))
print("IPs in subnet:")
printIPsInSubnet(ip, netmask)

# quote: Let the ipaddress libary do the work for you
print('\n-------------------------')
print('Using Import Address:')
network = ipaddress.ip_network(cidrNotation, strict=False)
print("IP:{}\tCIDR:{}".format(network, cidrSubnet))
print('subnet:{}'.format(network.netmask))
print('IPs in subnet:')

# Now we will ping each IP address, note we have to convert to string before we ping each.
for hosts in network.hosts():
    print(hosts)
    ipConvert = str(hosts)
    print(ping(ipConvert))
    print("\n-----------------------------------\n")

