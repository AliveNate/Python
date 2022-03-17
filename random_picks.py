
import random #create a random string
import string
# ===================================================================
# call:
# randomString(100) = 100char
def randomString(stringLength=10): # randomString() = default 10;

    """Generate a random string of fixed length = ex. dkwaloeckw"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
# ===================================================================

base = "00--" #Just the first chars on each line.
domains = ["gmail.com", "yahoo.com", "ucdenver.edu", "tesla.com", "outlook.com", "aol.com", "zoho.com"]
pwordSize = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

with open('file_dummyData.txt', 'w') as f:          # Open/create dummy file
    f.write('This is a dummy file, with usr/domain/password.')   # Write a single line to the file
    for i in range(1,1000):     # How many lines of text we want in file.

        f.write("\n" +     # This is all one line: [base]  [cryptUser]  [:]  [@]  [domain]  [cryptPass]
                base +
                randomString() + # base length of random a-z = 10    dkwaloeckw ex. username
                ":" +
                "@" +
                random.choice(domains) +    # random choose from domain list
                ":" +
                randomString(random.choice(pwordSize)))           # random crypt-pass, 10-20


