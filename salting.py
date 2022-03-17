"""
We see in our hashing and bruting programs that we can encode things like password into hashes.

Ex --> hasher.py
[*] Enter a string for us to hash:  'baseball'
md5     hash = 276f8db0b86edaa7fc805516c852c889

But these straightforward hashes can easily be copied/cracked.
If we add a sprinkle of salt, we can prevent the hash-recovery.
salting - add another word like a password to the original hash, and we can basically hash a hash

"""
#!/usr/bin/python3
import crypt

word = "admin"
cryptword = crypt.crypt(word, 'HX')     # HX = salt
print(f'{word} + HX = {cryptword}')      # = HXEL3zsoJxJ1E
#
cryptword = crypt.crypt(word, 'DL')     # DL = salt
print(f'{word} + DL = {cryptword}')      # = DLHarKEZk145I
# admin --> has 2 diff outcomes, but we see the salt value in front on both.
"""
So even though we can't auto complete another MD5 hash and discover the word like we normally could,
    we do know now that the first 2 letters are a salt. So we still may  be able to use 'DL' as a salt and then 
    replicate the rest of the hash.
    Try that in salting2.py....
"""



