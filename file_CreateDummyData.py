
import random #create a random string
import string
# ===================================================================
# call:
# randomString(100) = 100char
def randomString(stringLength=10): # randomString() = default 10;
    #Function to return a string of random lowercase a-z
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

'''EX
00--haxlsgbsdy:@gmail.com:lbdfezhpaf
00--gstawqmmtn:@ucdenver.edu:emokwjzmksgbjeprfdxv
00--kjqzzabkcl:@yahoo.com:dujkghqzkburhnexjjbi
00--kircqkftrj:@aol.com:jxfmalzlktbqpw
00--fmwasncunb:@zoho.com:hylapzjxlggs
00--pshdbchsgs:@aol.com:avcqhmmjutfv
00--qanvivoose:@outlook.com:wzxwzngjblqwqwz
00--erfzlxgvan:@yahoo.com:lzacdizwxsuzoguyausf
00--pwfgrbpeby:@zoho.com:furnbdlldojq
00--wdxnosaape:@gmail.com:gbzotwllssjitezpst
00--xcdjccbjkx:@gmail.com:arwomviulxlqsfegfnn
00--rvplrmswfa:@zoho.com:hhhumcxwaxqjojhex
00--mbwcptiuhx:@aol.com:jndxhtnkwvnkzgskobwv
'''

