#!/bin/python3
#------------------------------------------
#---Made by:   ./1scriptmaker.sh
#---This is:   scanner.py
#------------------------------------------
# Very simple scanner for a python 3 machine.
# Note - This program is not threaded. It will be slow.
#-----------------------------------------------------------
import sys #Allows us to enter command line arguments etc.
import socket #Need to connect to port/socket system.
from datetime import datetime #Simple to import pretty date.
#-----------------------------------------------------------

# Setup first argument, define our target
# Take an argument:    python3 scanner.py 192.168.3.1
# scanner.py = argument[0],
# 192.168.3.1 = argument[1]
#
if len(sys.argv) == 2: #If we have 2 arguments at execution (scanner.py 192.168.3.1)
	#If our machine is named "ncterry" we could use that, and this translates the name into IPv4
	target = socket.gethostbyname(sys.argv[1]) #Hostname=IPv4=2nd arguement=(sys.argv[1])
else:
	print("Invalid amount of arguments.")
	print("Syntax:   python3 scanner.py <ip>")
	sys.exit() #System will hang if we dont exit. Make sure user includes 2nd arg <ip>
#------------------------------------------------------
# Add a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
#------------------------------------------------------
try: #We need to grab ports. Remember this is simple/shitty version
	#We could add in another arg for specific ports, this is a simple example.
	for port in range(1, 1000): #Checking ports 1-1000
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Connection variable - AF_INET = IPv4, SOCK_STREAM = port
		socket.setdefaulttimeout(1) #Move on after 1sec if don't detect a port.
		#Take target from above <ip>, take port from for-loop. Check for result.
		result = s.connect_ex((target, port)) #If error on connection, return indicator. No error, return 0
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
#EX.
# Checking port 51
# Checking port 52
# Checking port 53
# Port 53 is open
# Checking port 54
#-------------------------------------------------------
# Add exceptions for errors that we know may happen.
#-------------------------------------------------------
except KeyboardInterrupt:
	print("\nKeyboard Interrupt - Exiting Program")
	sys.exit()
#-------------------------------------------------------
except socket.gaierror: #If we cannot connect to hostname
	print("Hostname could not be resolved.")
	sys.exit()
#-------------------------------------------------------
except socket.error:
	print("Could not connect to server.")
	sys.exit()
#-------------------------------------------------------

















