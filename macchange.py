"""Your machine's MAC address may be on a white/black list.
You can spoof that to bypass these list, or change it permanently.
Kali already has this:
                        # macchanger        macchanger --help

OneNote page about   'macchanger'  in Linux         """
#!/usr/bin/python3

import subprocess   # execute system commands

""" NOTE - the syntax for calls here had to be text, var, text
Normally we can use:        f'text {var} text'
But that gave us errors here, so we had to make it simple and avoid formatting.
"""
def change_mac_address(interface, new_mac_address):
    # 1) Shut interface down to make a permanent MAC change:        # ifconfig eth0 down
    # 2) Make the change:                   # ifconfig eth0 hw ether 11:22:33:44:55:66
    # 3) Turn interface back on to make a permanent change to MAC:  # ifconfig eth0 up
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def main():
    # check interfaces that the user has specified...ex - eth0
    interface = input(f'[*] Enter the interface to change the MAC address on. \nEX. \'eth0\':     ')
    new_mac_address = input(f'[*] Enter Mac Address to change to. \nEX: XX:XX:XX:XX:XX:XX:     ')

    # Check the output of the interface before change
    # before/after below are simply just:   # ifconfig eth0     (or interface other than eth0)
    # These are just to compare to see if  MAC  is different due to our change.
    before_change = subprocess.check_output(["ifconfig", interface])
    change_mac_address(interface, new_mac_address)
    after_change = subprocess.check_output(["ifconfig", interface])
    #
    if before_change == after_change:
        print(f'[!] Failed to Change MAC Address to: {new_mac_address}')
    else:
        print(f'[+] MAC Address Changed to: {new_mac_address} On Interface: {interface} ')

# -------------


main()


# -------------
# -------------
