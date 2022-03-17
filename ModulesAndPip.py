
'''

We have a function that rolls dice below.
Send the number, and it rolls a dice up to that number.

We have another program that wants to use the dice.
WE could just copy and paste the fuction, but if we have this file saved,
    then we can just import this whole file, and then use:    roll_dice


import ModulesAndPip

Then from the other file, to use  roll_dice

ModulesAndPip.roll_dice(6)
========================================================

List of previously created modules.
https://docs.python.org/3/py-modindex.html

Just google python modules
'''

import random
#
feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "Ringo Start", "George Harrison"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
