"""
'baseball' is a password in our target file.
We are assuming that we dont know that, but we are bringing in a md5 hash that we found.
We created the md5 hash earlier in 'hasher.py' so we would use it here.
#
[*] Enter a string for us to hash:  'baseball'
md5     hash = 276f8db0b86edaa7fc805516c852c889

Now we will enter that MD5 hash in this program
And we will enter the location of our password file.
And see if we get any results.
"""

#!/usr/bin/python3
#
# Imports---------------------
from termcolor import colored
import hashlib
# ----------------------------

def TryOpen(wordlist):
    global passfile     # Make global so we can use it in the external for loop
    try:
        passfile = open(wordlist, 'r')
    except:
        print(f'[!] No Such Path To That File')
        quit()


# ------------------------------------------------
#
# Prompt user
passhash = input(f'[*] Enter the MD5 Hash Value: ')
wordlist = input(f'[*] Enter the Path to the Password File: ')

TryOpen(wordlist)

for word in passfile:
    print(colored("[*] Trying " + word.strip('\n'), 'red'))
    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    print(f'md5digest = {md5digest}')   # Just to see what each new md5 is
"""
hash.hexdigest() - the digest is returned as a string object of double length, containing only hexadecimal digits.
This may be used to exchange the value safely in email or other non-binary environments.
"""

    if md5digest == passhash:
        print(colored("[+] Password Found: " + word, 'green'))
        exit(0)

print(f'[!] Password Not in List.')


"""
[*] Enter the MD5 Hash Value: 276f8db0b86edaa7fc805516c852c889
[*] Enter the Path to the Password File: bruteforceMD5pwds.txt

[*] Trying 123456
md5digest = e10adc3949ba59abbe56e057f20f883e
[*] Trying dragon
md5digest = 8621ffdbc5698829397d97767ac13db3
[*] Trying 123123
md5digest = 4297f44b13955235245b2497399d7a93
[*] Trying baseball
md5digest = 276f8db0b86edaa7fc805516c852c889
[+] Password Found: baseball
"""