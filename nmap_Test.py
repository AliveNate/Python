# Execute:       
#		python nmap_Test.py


import nmap
nmap1 = nmap.PortScanner()

a = nmap1.nmap_version()

print(a)
