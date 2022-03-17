# Run this file in PyCharm or etc.
# Prints well, an is easy to read.

# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print("\nTrick 5") # ============
print("Enumerator count with 2 lists")
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for index, name in enumerate(names):
    print(f'{name} is actually {heroes[index]}')
'''
Peter Parker is actually Spiderman
Clark Kent is actually Superman
Wade Wilson is actually Deadpool
Bruce Wayne is actually Batman
'''
# ----------------------------------
print("\nSecond option:")
# Note: ZIP will end at the shortest list.
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')
'''
Peter Parker is actually Spiderman from Marvel
Clark Kent is actually Superman from DC
Wade Wilson is actually Deadpool from Marvel
Bruce Wayne is actually Batman from DC
'''
# ----------------------------------
print("\nThird option:")
for values in zip(names, heroes, universes):
    print(values)
'''
('Peter Parker', 'Spiderman', 'Marvel')
('Clark Kent', 'Superman', 'DC')
('Wade Wilson', 'Deadpool', 'Marvel')
('Bruce Wayne', 'Batman', 'DC')
'''
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print("\nTrick 6") # ============
print("Unpacking...")
print("What if we import a list, but only need the first value."
      "\nWe will get an error, if we don't catch the second value."
      "\nAdd an underscore, and it will negate the second value.")
a, _ = (1, 2)
print("a, _ = (1, 2)")
print(f'a = {a}')
# a = 1
# ---------------------
print("\nSet extras on an import to a spare Var")
print("Catch a and b, and set c to catch all the rest")
print("a, b, *c = [1, 2, 3, 4, 5]")
a, b, *c = [1, 2, 3, 4, 5]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
'''
a = 1
b = 2
c = [3, 4, 5]

'''
# ---------------------
print("\nSet extras on an import to a spare Var example 2")
a, b, *c, d = [1, 2, 3, 4, 5]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
'''
a = 1
b = 2
c = [3, 4]
d = 5

'''
# ---------------------
print("\nSet extras on an import to a spare Var example 3")
print("Ignore import values")
a, b, *_, d = [1, 2, 3, 4, 5, 6, 7]
print(f'a = {a}')
print(f'b = {b}')
#print(f'c = {c}')
print(f'd = {d}')
'''
a = 1
b = 2
d = 7

'''
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print("\nTrick 7") # ============
print("Run this program from Terminal:  # python TRICKS.py"
      "\nWhen it asks for password, we want that hidden.")
print("For the password, instead of  input  use  getpass.")
from getpass import getpass
username = input("Username: ")
password = getpass("Password: ") # In terminal we don't want a shoulder surfer seeing the password.
# getpass does not work in pycharm. Only in Terminal. Shows a Key Symbol

print("Logging in....")
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
