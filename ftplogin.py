"""
This is a simple ftp login on an IPv4
If there are any regulations on the target, this will not work.
It simply tries to FTP connect. No username, no password, etc
"""
#!/usr/bin/python

import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymus', 'anonymus')
        print(f'[*] {hostname} FTP Anonymus Logon Succeeded.')
        ftp.quit()
        return True
    # --------------------
    except Exception as e:
        print(f'[-] {hostname} FTP Anonymus Logon Failed')


host = input("Enter the IP address: ")
anonLogin(host)
