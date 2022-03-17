"""
This program is a simple implementation of creating several common hash values.
User enters a string:
String is encoded into several types of hashes.
"""

#!/usr/bin/python3

import hashlib  # Allows us to perform the hashing

"""
hash.hexdigest() - the digest is returned as a string object of double length, containing only hexadecimal digits.
This may be used to exchange the value safely in email or other non-binary environments.
"""
hashvalue = input(f'[*] Enter a string for us to hash: ')
# --------------------------------------------------------
hashobject1 = hashlib.md5()             # Create an object to hold the md5 hash
# We want to encode the input-string, on the md5 hash object, based on the hex-digest function.
hashobject1.update(hashvalue.encode())  # Be able to add the hashvalue to the hashobject
print(f'md5     hash = {hashobject1.hexdigest()}')
# --------
hashobject2 = hashlib.sha1()            # Create object to hold the SHA1 hash
hashobject2.update(hashvalue.encode())
print(f'sha1    hash = {hashobject2.hexdigest()}')
# --------
hashobject3 = hashlib.sha224()            # Create object to hold the SHA1 hash
hashobject3.update(hashvalue.encode())
print(f'sha224  hash = {hashobject3.hexdigest()}')
# --------
hashobject4 = hashlib.sha256()            # Create object to hold the SHA1 hash
hashobject4.update(hashvalue.encode())
print(f'sha256  hash = {hashobject4.hexdigest()}')
# --------
hashobject5 = hashlib.sha512()            # Create object to hold the SHA1 hash
hashobject5.update(hashvalue.encode())
print(f'sha512  hash = {hashobject5.hexdigest()}')
# --------
"""Ex: 
[*] Enter a string for us to hash: p@ssword123

md5     hash = 9546368a81dea9bfda8218b5873c4a7d
sha1    hash = 0c95b3614c839fab66443b64099338b09417b697
sha224  hash = 01ceb4328453272d0061260f1ef0c95c966d19c00bffebb50fb97dbc
sha256  hash = f55d184f3df1b47eca0d5390baf23ba2299bc626bf27209b6fb534faf8af258b
sha512  hash = ebb00d7fd7e765d97c723ccd20aeb483e18e6d96c0194efe3b525773c37131a26178d5b0f55506c9c95592cf9f4896df9fef7f93ae812fe32dcc6a6cccbbf3ed

- Note - The simple md5 hash is not very secure. 
If you simply paste that md5 hash into google, it will return Nate from numerous sites.
"""