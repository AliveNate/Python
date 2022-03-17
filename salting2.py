"""In    salting.py    we have a basic example of how to salt a hash.
This program here is how to try and crack that hash/password if we discover what 'salt' was used.
We discover a hashed value in a user:password list.     GHpzDyyNFUBeU
We know that the salt is the first 2 letters            GH
We can use that, and also a common password list to try and re-create this current salted-hash.
Target File =
                        root:password
                        ncterry:GHpzDyyNFUBeU
                        admin:root
# word = "basketball"                                   # our password, which is also in the password list file.
# We can encrypt a password, with a 2-letter salt.
# enc_word = crypt.crypt(word, 'GH')                    # GH is the salt
# print(f'basketball + GH = {enc_word}')                #  = GHpzDyyNFUBeU
"""
#!/usr/bin/python3
import crypt    # Uses DES with an optional salt
from termcolor import colored

def crackPass(cryptword):
    # The salt is not necessarily the first 2 letters, but we know this one, it is just a simple example
    salt = cryptword[0:2]   # Take salt from hash-word. 1st 2 letters[0:2] (0,1,2) remem the last value [2] is ignored.
    dictionary = open('salting2pwdlist.txt', 'r')   # The list of most common passwords
    for word in dictionary.readlines():             # Read every potential password
        word = word.strip('\n')                     # Strip the newline from each
        cryptpass = crypt.crypt(word, salt)         # Encrypt the password, WITH the known 2letter salt.
        if (cryptword == cryptpass):                # If our new hash+salt == the original that we are testing....
            print(colored("[+] Found Password: " + word, 'green'))
            print(f'---------Salt       = {salt}')
            print(f'---------cryptword  = {cryptword}')
            print(f'---------password   = {word}')
            return word


def main():
    # This is a list of:    user:password
    passfile = open('salting2userpwds.txt', 'r')    # Ex:   root:GHpzDyyNFUBeU
    for line in passfile.readlines():               # Read each line
        if ":" in line:                             # Look for colon that we know separates  user:password
            user = line.split(':')[0]               # Grabs root from:       root:GHpzDyyNFUBeU
            cryptword = line.split(':')[1].strip(' ').strip('\n')  # Get password, and also strip any spaces OR newlines
            print(colored("[*] Cracking Password for: " + user, 'red'))
            print(f'{user} / {crackPass(cryptword)}')  # Run cracking function and print return value in same command.


main()


"""Example:

[*] Cracking Password for: admin
admin / None

[*] Cracking Password for: adminmsf
adminmsf / None

[*] Cracking Password for: admintmp
admintmp / None

[*] Cracking Password for: ncterry
[+] Found Password: basketball
---------Salt       = GH
---------cryptword  = GHpzDyyNFUBeU
---------password   = basketball
ncterry / basketball

[*] Cracking Password for: roottmp
roottmp / None

[*] Cracking Password for: rootmsf
rootmsf / None

[*] Cracking Password for: root
[+] Found Password: mustang
---------Salt       = DL
---------cryptword  = DLQDYCL4oQLwM
---------password   = mustang
root / mustang

[*] Cracking Password for: adminfake
adminfake / None
"""

