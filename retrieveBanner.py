"""
Execute with simple:    # python3 retrieveBanner.py
"""
#!/usr/bin/python3


"""
Code is similar to a port scanner.
When we connect to the ports, we want to get data from the ports.
If they send those bytes, we can get info like software they are running etc.
"""
# ------------------------------------
# ------------------------------------
# Imports
import socket
# ------------------------------------
# Connect to port, gather return data from that port if connected.
# Banner info from that port may give us helpful info.
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2) # Don't hang up on a single port
        s = socket.socket()         # Create a socket object
        s.connect((ip, port))       # Connect to a port, on an IP
        banner = s.recv(1024)       # Capture 1024 bytes from return data
        return banner
    except:             # in case try doesnt work.
        return

# ------------------------------------
# ------------------------------------
def main():
    ip = input("[*] Enter target IP: ")
    for port in range(1, 100):
        banner = retBanner(ip, port)
        if banner:  # Exists
            print(f'{ip} : {port} : {banner}')
        else:
            print(f'No banner for port {port} retrieved.')
    # ------------------------------------
# ------------------------------------

main()

# Sample banner returned:
#       192.168.1.5 SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
# We can used that banner info to help research the target.
