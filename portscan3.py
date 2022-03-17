#!/usr/bin/python3
#
# We started with 'portscan1 --> portscan2.py -->'
# The are all similar, but progress as advanced.
# ----------------------------
# ----------------------------
# Imports
from socket import *     # Import all methods from the socket library
import optparse          # Library lets us create/indicate execution options to the user.
from threading import *  # We want each port to be scanned by a different thread.
# ____________________________Otherwise it will take much longer if every port is scanned by a single thread.
# ----------------------------
# ----------------------------
# ----------------------------
# ----------------------------
def connScan(tgtHost, tgtPort):
    try:  # AF_INET=IPv4,   SOCK_STREAM=tcp
        sock = socket(AF_INET, SOCK_STREAM)  # Don't need "socket."  'socket.AF_INET...since we imported ALL
        sock.connect((tgtHost, tgtPort))     # Need double parens
        print(f'{tgtPort} /tcp Open')
    except:
        print(f'{tgtPort} /tcp Closed')
    finally:
        sock.close()                         # Make sure to close the host/port connection.

# -------------------------------
# ------------------------------
# -------------------------------
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)      # Pulls the IP from host, such as www.google.com
    except:
        print(f'Unknown host: {tgtHost}')   # We don't want a program crash if it can't resolve the IP
    # ------------------------------------
    try:
        tgtName = gethostbyaddr(tgtIP)              # Actually get the host by name, from the address.
        print(f'Scan Results for: {tgtName[2]}')    # tgtName is retrieved as a list. Be Careful (below)
        """
        Return results to show List Example for:   www.ncterry.com:
        tgtName[0] --> Scan Results for: pages-custom-13.weebly.com
        tgtName[1] --> Scan Results for: ['57.228.34.199.in-addr.arpa']
        tgtName[2] --> Scan Results for: ['199.34.228.57']
        """
    except:
        print(f'Scan Results for: {tgtIP}')
        #
    setdefaulttimeout(1)        # Dont wait too long for a single port.
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))  # Function scan ports, but using different threads.
        t.start()
# ==================================================================================
def main():
    """
        If you run the program:
                # python3 portscan3.py -H 10.0.0.114 -p 443
        But you don't execute properly, or if you run in pycharm, it will simple just return that first line:
                "Usage of program: -H <target host> -p <target ports"
        The     parser.add_option    allows us to include stated args, and assign them local names.

Example on Site:
nct@NCT-5 Python %      python3 portscan3.py -H www.ncterry.com -p 135,443,80
        Scan Results for: pages-custom-13.weebly.com
        443 /tcp Open
        80 /tcp Open
        135 /tcp Closed
    """
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target ports separated by comma')
    # Execute      python3 portscan3.py -H 10.0.0.114 -p 443
    (options, args) = parser.parse_args()  # options(-H, -p)   args(10.0.0.114, 443)
    # Specify our dest=variables that we used above
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    # Line above lets us enter numerous ports for the arg. But can only be separated by just a comma, no space
    #        python3 portscan3.py -H 10.0.0.114 -p 135,443,80,1234
    #
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)  # Applies to the first line above,    parser =
        exit(0)
    portScan(tgtHost, tgtPorts)  # Call portScan function, which in turn calls the connScan function
# ==================================================================================================
if __name__ == '__main__':
    main()  # Run
"""
This program is built to run by standard execution.
Just PyCharm play will not do anything.
    # python3 portscan3.py -H 10.0.0.114 -p 135
            Scan Results for: 10.0.0.114
            135 /tcp Closed
"""
