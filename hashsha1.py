"""
This program is gathering 10000 commonly used passwords from a git repo
We also have those 10000 passwords here on a txt file:   '10000passwords.txt'
A common password on that list = 'baseball'
To test this out, we are going into our other program:   hasher.py
Run that and enter 'baseball'
One of the sendbacks, is the SHA1 hash of 'baseball'

    baseball --> SHA1 = a2c901c8c6dea98958c219f6f2d038c44dc5d362

We run this program, and enter that SHA1-hash for 'baseball'
The  for  loop cycles through every line in the 10000 passwords
Converts them to SHA1, and compares each to our 'baseball' hash input.
If our 'baseball' SHA1-hash input matches the SHA1-hash our program also creates for a line,
    then we can determine that since our SHA1-hash matches, then the original password is our answer

"""

#!/usr/bin/python3
# -----------------------------------
from urllib.request import urlopen      # To bring in password list from URL
import hashlib
from termcolor import colored
# -----------------------------------
sha1hash = input(f'[*] enter SHA1 Hash Value: ')  # baseball --> SHA1 = a2c901c8c6dea98958c219f6f2d038c44dc5d362
#
# Open url for password list on github
# Treat it as a file and read() it, and assume we can treat it as  utf-8 format
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
#
"""2nd Line Below the guess is like:  a2c901c8c6dea98958c219f6f2d038c44dc5d362
hashlib takes password from file, which is in utf-8 format, and encodes it in SHA1
There are many more options other than SHA1
"""
"""
hash.hexdigest() - the digest is returned as a string object of double length, containing only hexadecimal digits.
This may be used to exchange the value safely in email or other non-binary environments.
"""
for password in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()  # change each line/password into SHA1 encoding
    #hashguess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()  # change each line/password into SHA1 encoding
    #hashguess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()  # change each line/password into SHA1 encoding
    if hashguess == sha1hash:   # if a file line in SHA1 ==  original SHA1 input, we then know what the password is
        print(colored("[+] The Password is: " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] Password Guess: " + str(password) + " does not match. Trying next...", 'red'))

# -----------------------------------------------
# If no SHA1 password matches are found.
print(f'Password is not in the password list.')
# -----------------------------------------------

"""
Example:  

[*] enter SHA1 Hash Value: a2c901c8c6dea98958c219f6f2d038c44dc5d362

[-] Password Guess: 123456 does not match. Trying next...
[-] Password Guess: password does not match. Trying next...
[-] Password Guess: 12345678 does not match. Trying next...
[-] Password Guess: qwerty does not match. Trying next...
[-] Password Guess: 123456789 does not match. Trying next...
[-] Password Guess: 12345 does not match. Trying next...
[-] Password Guess: 1234 does not match. Trying next...
[-] Password Guess: 111111 does not match. Trying next...
[-] Password Guess: 1234567 does not match. Trying next...
[-] Password Guess: dragon does not match. Trying next...
[-] Password Guess: 123123 does not match. Trying next...
[+] The Password is: baseball
"""