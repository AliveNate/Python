
# Note
# I initally created this file as   random.py
# The built in module is already named  random.py
# Got errors until i renamed this file.


import random # Random is a built in module
                # external libraries / python3.7 /python 3.7 library root / random.py (and others)
# --------------------
# --------------------

for i in range(3):
    print(random.random())  #random values 3times, 0-1
# --------------------
for i in range(3):
    print(random.randint(10, 20))  # random values 3times, 0-1
# --------------------
# --------------------

members = ["John", "Mary", "Bob"]
leader = random.choice(members)
print("Leader = " + leader)
# --------------------
# --------------------

# Roll a random pair of dice
class Dice:
    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1, d2

dice = Dice()
print(dice.roll())
# --------------------
# --------------------
