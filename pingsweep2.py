from scapy.all import *
import netaddr

# Define IP range to ping
network = "10.0.2.0/24"#"172.16.20.0/24"

# make list of addresses out of network, set live host counter
addresses = netaddr.IPNetwork(network)
liveCounter = 0

# Send ICMP ping request, wait for answer
for host in addresses:
	if (host == addresses.network or host == addresses.broadcast):
		continue
	resp = sr1(IP(dst=str(host))/ICMP(),timeout=2,verbose=0)
	if (str(type(resp)) == "<type 'NoneType'>"):
		print str(host) + " is down or not responding."
	elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
	        print str(host) + " is blocking ICMP."
	else:
		print str(host) + " is responding."
		liveCounter += 1

print "Out of " + str(addresses.size) + " hosts, " + str(liveCounter) + " are online."
