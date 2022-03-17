
# This is an exact copy of sshlogin.py, but without the notes.

# This is the same code as   sshlogin.py  but without the notes.
#!/usr/bin/python3
# Imports
import pexpect  # Had to install also

# After password, we would expect a return prompt (options) from the target machine meaning that we are logged in.
PROMPT = ['#', '>>>', '>', '\$']


def send_command(child, command):       # child  AKA  the connection
    # Send the connection, and the command to use on that connection
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)  # print the output of the command we used on the target system


def connect(host, user, password):
    ssh_newkey = "Are you sure you want to continue connecting"  # question from trying to ssh into target
    connStr = "ssh " + user + "@" + host     # EX.    ssh ncterry@10.0.2.7
    child = pexpect.spawn(connStr)  # Send ssh command to target
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
    child.expect(PROMPT)
    return child


def main():
    host = input("Enter the target IP: ")                        # "10.0.2.7"   # Target IP
    user = input("Enter the SSSH username on the target IP: ")   # ncterry    # Target user, on target IP
    password = input("Enter the SSH password: ")
    child = connect(host, user, password)   # Created function to ssh in, and return info
    send_command(child, 'cat /etc/shadow | grep root')
    send_command(child, 'ls -lha')
# ---------------------------------------------------------
# ---------------------------------------------------------


main()


