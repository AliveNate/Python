

#!/usr/bin/python3
"""
This establishes a connection to another IP
Then scans that IP for several ports that we have listed.
If the port is open, it will send back response data.
We collect the first 1024 bytes of that data, and save as a banner.
We also have a local text file with info.
If the data that we get from the banner, (open port) matches a line in the txt file,
    then we know that the target host is potentially vulnerable.
"""
# Execute:
# NOTE - This has some issues in byte-syntax with python3. Run with python2
#           python vulnScan.py vulnbanners.txt
# -------------------
# Imports
import socket
import os   # Has functions to let us check if file exists.
import sys  # check out the number of args needed for the program
# --------------------
# main() --> retBanner() --> checkVulns()
# ---------------------------------------------------------------------------------
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
# ---------------------------------------------------------------------------------
# This function is called from the bottom of main()
# We have a txt file next to this py file.
# That txt file has line in it, once of which is:
#       SSH-2.0-OpenSSH_8.1p1 Debian-5
# We read through this file, line by line.
# If a line in the txt file, matches (is in) the banner info, then print the vulnerability.
#   [+] Server is vulnerable: SSH-2.0-OpenSSH_8.1p1 Debian-5
#
def checkVulns(banner, filename):
    f = open(filename, "r")  # open file, and just read it.
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable: " +  banner.strip('\n'))

# ---------------------------------------------------------------------------------
def main():
    # sys library to check if we have the correct number of args from execution.
    # Need 2 args = this file, and the target text file.
    if len(sys.argv) == 2:  # if there are 2 args
        filename = sys.argv[1] # then the target file is the second one.
        if not os.path.isfile(filename):     # Check if target file does not exist
            print(filename + " does not exist.")
            exit(0)
        if not os.access(filename, os.R_OK):  # Check is user has permissions for that file.
            print("Access Denied!")
            exit(0)
    #
    else: # python vulnScan.py          --> only 1 arg, get this error message.
        print("Execute: python " + str(sys.argv[0]) + " <vuln filename>")  # Instructions if user does not run correctly.
        exit(0)

    #
    # Search these ports, on the listed hosts, we have just 10.0.2.6, 10.0.2.7 now.
    # If an open port in this list, returns data, the first 1024 bytes are saved as a banner.
    #       Ex.     10.0.2.6 : 22 : SSH-2.0-OpenSSH_8.1p1 Debian-5
    #
    portlist = [21, 22, 25, 80, 110, 443, 445]  # List of most used ports to scan on target hosts.
    for x in range(5, 8):  # Loop through VMs on network, 10.0.2.x, 10.0.2.6, 10.0.2.7........
        ip = "10.0.2." + str(x)   # 10.0.2. = the subnet on our local network
        print(ip)
        for port in portlist:
            print(ip + " : " + str(port))
            banner = retBanner(ip, port)  # if port is open, gather the response data
            if banner:  # if the banner was actually returned from the port.
                print(ip + " : " + str(port) + " : " + banner)
                checkVulns(banner, filename)  # Check to see if banner data, matches line in txt file.
# ---------------------------------------------------------------------------------

main()

# 1) Execute + py-file + target-file
# 2) Print the return data from an open port
# 3) Check if return data, matches line in text file.
"""root@kali:/media/sf_KaliSecurity/Python# python vulnScan.py vulnbanners.txt 

10.0.2.6 : 22 : SSH-2.0-OpenSSH_8.1p1 Debian-5

[+] Server is vulnerable: SSH-2.0-OpenSSH_8.1p1 Debian-5

root@kali:/media/sf_KaliSecurity/Python# 

==============================================
Scan 3 machines, 2 are active
10.0.2.6 and 10.0.2.7 are active machines, and only port 22 is open on both
We acknowledge that ip + open port, and the return banner data for both.

10.0.2.5
10.0.2.5 : 21
10.0.2.5 : 22
10.0.2.5 : 25
10.0.2.5 : 80
10.0.2.5 : 110
10.0.2.5 : 443
10.0.2.5 : 445
10.0.2.6
10.0.2.6 : 21
10.0.2.6 : 22
10.0.2.6 : 22 : SSH-2.0-OpenSSH_8.1p1 Debian-5

[+] Server is vulnerable: SSH-2.0-OpenSSH_8.1p1 Debian-5
10.0.2.6 : 25
10.0.2.6 : 80
10.0.2.6 : 110
10.0.2.6 : 443
10.0.2.6 : 445
10.0.2.7
10.0.2.7 : 21
10.0.2.7 : 22
10.0.2.7 : 22 : SSH-2.0-OpenSSH_7.4

[+] Server is vulnerable: SSH-2.0-OpenSSH_7.4
10.0.2.7 : 25
10.0.2.7 : 80
10.0.2.7 : 110
10.0.2.7 : 443
10.0.2.7 : 445
"""
