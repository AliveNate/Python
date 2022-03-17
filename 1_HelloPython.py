import random
import sys
import os

# use the Run in the top menu bar. Run -> Run
print("Hello World")  # this will print out the Hello World String
print("---------------------------------------------------------")
print("---------------------------------------------------------")

# to make a comment use the hash symbol
'''
multiline comment is in between the
    3x3 single quotes
'''

# This is a standard string variable
name = "Nate"  # standard variable
print(name)  # this will print out our string variable.

print("---------------------------------------------------------")
print("---------------------------------------------------------")
# 5 main data types -> variable name has to start with a letter
# strings, numbers, lists, tuples, Dicitonaries.
print("---------------------------------------------------------")
print("---------------------------------------------------------")
# 7 different arithmetic operators
# + - * / % ** //
# ** is the exponential and // is floor division which get rid of the excess from a division.
print("---------------------------------------------------------")
print("----------------order of operations, arithmetic----------")
# order of operation matters
print(" 1 + 2 - 3 * 2 = ", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 = ", (1 + 2 - 3) * 2)
print("---------------------------------------------------------")
print("---------------quote and multiline quote-----------------")
quote = "\"Always remember you are unique"
multi_line_quote = ''' just
like everyone else'''
print(multi_line_quote)
'''
 just
like everone else
'''
print("---------------------------------------------------------")
print("---------join two quotes into one variable----------------")
to_join_quotes = quote + multi_line_quote
print(to_join_quotes)
'''
Always rememebr you are unique just
like everone else
'''
print("--------------------------print two quotes indirectly----")
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
'''
I like the quote "Always rememebr you are unique  just
like everone else
'''
print("---------------------------------------------------------")
print("--------------------ignore new lines---------------------")
print("I don't like", end=" ")
print("newlines")
'''
I don't like newlines
'''
print("---------------------------------------------------------")
print("------auto include a new line with backslash n * 5 will bring 5 new lines----------")
print("\n" * 5)
print("see 5 empty lines above")
'''






see 5 empty lines above
'''
print("---------------------------------------------------------")
print("--------------on to lists, display will contain quotes on ------")
grocery_list = ['Juice', 'Tomatores', 'Potatoes', 'Bananas']
print("First Item = ", grocery_list[0])
print(grocery_list[1:3])
'''
First Item =  Juice
['Tomatores', 'Potatoes']
'''
print("---------------------------------------------------------")
print('\n', "--------------can combine lists -------------------")
other_events = ["wash car", "pick up girls"]
to_do_list = [other_events, grocery_list]
print(to_do_list)
'''
[['wash car', 'pick up girls'], ['Juice', 'Tomatores', 'Potatoes', 'Bananas']]
'''
print("---------------------------------------------------------")
print('\n', "-------------add to list---------------------------")
print(grocery_list)
grocery_list.append("Onion")
print(grocery_list)
'''
['Juice', 'Tomatores', 'Potatoes', 'Bananas']
['Juice', 'Tomatores', 'Potatoes', 'Bananas', 'Onion']
'''
print("---------------------------------------------------------")
print('\n', "-------------insert to list------------------------")
print(grocery_list)
grocery_list.insert(2, "Ice Cream")
print(grocery_list)
'''
['Juice', 'Tomatores', 'Potatoes', 'Bananas', 'Onion']
['Juice', 'Tomatores', 'Ice Cream', 'Potatoes', 'Bananas', 'Onion']
'''
print("---------------------------------------------------------")
print('\n', "-------------tuples--------------------------------")
# similar to list, but cannot change after created
pi_tuple = (3, 1, 4, 1, 5, 9)
new_tuple = list(pi_tuple)
new_list = tuple(pi_tuple)
print("---------------------------------------------------------")
print("We have a tuple, changed into list, and back into tuple. Can change list not tuple")
print(pi_tuple)
print(new_tuple)
print(new_list)
length_tuple = len(pi_tuple)
print("length of tuple = ", length_tuple)
print("min in tuple = ", min(pi_tuple))
print("max in tuple = ", max(pi_tuple))
'''
We have a tuple, changed into list, and back into tuple. Can change list not tuple
(3, 1, 4, 1, 5, 9)
[3, 1, 4, 1, 5, 9]
(3, 1, 4, 1, 5, 9)
length of tuple =  6
min in tuple =  1
max in tuple =  9
'''
print("---------------------------------------------------------")
print('\n', "-------------Dictionary or Map---------------------")
print("Similar to lists but cannot join them together")
super_villians = {"Fiddler": "Mark", "Joker": "Zach", "WonderWoman": "Ben"}
print(super_villians)
# {'Fiddler': 'Mark', 'Joker': 'Zach', 'WonderWoman': 'Ben'}

print("Dictionary acts like a word + definition. Print the word and it will actually print the definitaion")
# ---------------------------------------
print("Example:   print(super_villians['Fiddler'])")
# Example:   print(super_villians['Fiddler'])
print(super_villians["Fiddler"])  # will be "Mark"
# Mark
# ---------------------------------------
# change a specific object in the dictionary
super_villians['Fiddler'] = 'Markus'
# ---------------------------------------
# changed "Fiddler" so print again to show
print(super_villians.get('Fiddler'))  # now will be Markus
# Markus
# ---------------------------------------
# print the length of the dictionary
print(len(super_villians))
# 3
# ---------------------------------------
# this just prints the individual keys in this dictionary.
print(super_villians.keys())
# dict_keys(['Fiddler', 'Joker', 'WonderWoman'])
# ---------------------------------------
# printing the values which correspond to the keys
print(super_villians.values())
# dict_values(['Markus', 'Zach', 'Ben'])
# ---------------------------------------
# how to delete a specific dictionary key/value
del super_villians['Fiddler']
# ---------------------------------------
# printing the dictionary after deleting one.
print(super_villians)
# {'Joker': 'Zach', 'WonderWoman': 'Ben'}
# ---------------------------------------
'''
Similar to lists but cannot join them together
{'Fiddler': 'Mark', 'Joker': 'Zach', 'WonderWoman': 'Ben'}
Dictionary acts like a word + definition. Print the word and it will actually print the definitaion
Example:   print(super_villians['Fiddler'])
Mark
Markus
3
'''
print("---------------------------------------------------------")
print('\n', "-----------------Conditionals------------------------------")
# a simple if/else
# remember you need the colons
age = 21
if age > 16:
    print("You are old enough to drink")
else:
    print("You are not old enough to drink")
    '''
    You are old enough to drink
    '''
# ----------------------------------------------------------
if age >= 21:
    print("You can drink & drive")
elif age >= 16:
    print("You can only drive sober")
else:
    print("You can't drink OR drive")

'''
You can drink & drive
'''
print("---------------------------------------------------------")
print('\n', "------------------Conditions with logical operators-----------------------------")

if ((age >= 1) and (age <= 18)):
    print("You get a birthday lap dance")
elif (age == 21) or (age >= 65):
    print("The stripper has to be a guy")
else:
    print("You just get a simple cake")
'''
The stripper has to be a guy
'''
print("---------------------------------------------------------")
print('\n', "---------------Looping--------------------------------")
# this is a for loop that goes from 0 to <10. Ten spots but technically 0 ->9
# this will print the x value and a space from 0 to the end of the loop
for x in range(0, 10):
    print(x, " ", end=" ")
'''
0   1   2   3   4   5   6   7   8   9

'''
print("---------------------------------------------------------")
print('\n')
# we have pre-defined the grocery list above
# not sure how y accounts for the objects inside the list
for y in grocery_list:
    print(y)
'''
Juice
Tomatores
ice Cream
Potatoes
Bananas
onion
'''
print("---------------------------------------------------------")
print('\n')
for x in [2, 4, 6, 8, 10]:
    print(x)
'''
2
4
6
8
10
'''
print("---------------------------------------------------------")
print('\n')
# this double for loop prints out all
# remember y 123 then x++ then y 10 20 30 then x++ then y 100 200 300
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
'''
1
2
3
10
20
30
100
200
300
'''
print("---------------------------------------------------------")
print('\n', "--------------While loop---------------------------------")
# we imported random up top
# this first line will just do the random once
random_num = random.randrange(0, 100)
# we need to include the random_num = below the loop to work
# or else it will just be the single value above and cycle forever if not 15
while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)
'''
89
12
17
55
67
74
98
7
62
20
19
52
7
32
34
76
37
68
66
97
89
38
52
73
23
18
79
81
37
68
99
95
16
7
61
75
46
50
11
36
75
3
79
84
16
35
6
77
49
16
33
7
41
75
78
7
66
87
62
2
4
35
7
32
25
95
44
91
91
95
82
77
7
34
21
51
26
48
28
93
34
97
76
'''

print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print('\n')
print("\n--------------While loop with iterator and conditions---------------------------------")

i = 0

while i <= 20:
    if i % 2 == 0:
        print(i)
        i += 1
        # should only print if the i is even since using mod2
    elif i == 9:
        break
        # this will break out of the whole loop once i = 9
    else:
        i += 1
        continue
        # ex. 3<9 but mod2 != 0 and we still have to increase i
'''
0
2
4
6
8
'''

print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print('\n', "-------------functions----------------------------------")
print("simple function returns the sum of two parameters")


def addnumber(fNum, lNum):
    sumnum = fNum + lNum
    return sumnum


print(addnumber(1, 4))
'''
5
'''
print("---------------------------------------------------------")
print('\n', "--------------#input from user---------------------")
# input from user - Two ways to get the same input
print("What is your name?")
name = sys.stdin.readline()
print("Hello", name)
#
print("What is your new name?")
newname = input()
print("Hello", newname)
print("---------------------------------------------------------")
print('\n', "-----------strings---------------------------------")
long_string = "i'll catch you if you fall = The Floor"
# ---------------------------------------
# print the first 4 characters
print(long_string[0:4])
'''i'll'''
# ---------------------------------------
# print the last 5 characters
print(long_string[-5:])
'''Floor'''
# ---------------------------------------
# print all the way up to the last 5 characters
print(long_string[:-5])
'''i'll catch you if you fall = The '''
# ---------------------------------------
# print up to the 4th char and then add extra
print(long_string[:4] + " be there")
'''i'll be there'''
# ---------------------------------------
# complecated
# print("%c is my %s letter adn my number &d number is %.5f" % ('X', 'favorite', 1, .14))
# ---------------------------------------
# capitalize the first letter
print(long_string.capitalize())
'''I'll catch you if you fall = the floor '''
# ---------------------------------------
# return the index value of the start of the string -> starts at 33
print(long_string.find("Floor"))
''' 33'''
# ---------------------------------------
# is everything a letter in the string
print(long_string.isalpha())
''' False'''
# ---------------------------------------
# is everything a number in the string
print(long_string.isalnum())
''' False'''
# ---------------------------------------
# length of string
print(len(long_string))
''' 38'''
# ---------------------------------------
# replace part of string
print(long_string.replace("Floor", "Ground"))
''' i'll catch you if you fall = The Ground'''
# ---------------------------------------
# strip out whitespace from string (fyi no whitespace here anyway)
print(long_string.strip())  # not sure about this one
'''i'll catch you if you fall = The Floor'''
# ---------------------------------------
# turn a string into a list word by word
quote_list = long_string.split(" ")
print(quote_list)
''' ["i'll", 'catch', 'you', 'if', 'you', 'fall', '=', 'The', 'Floor']'''
print("---------------------------------------------------------")
print('\n', "------------File input/output----------------------")
# open a file, include the "wb" if you want to write to the file
test_file = open("1_HelloPython.txt", "wb")
# ---------------------------------------
# output on the screen the file mode
print(test_file.mode)
'''wb'''
# ---------------------------------------
# if I want to print the file name
print(test_file.name)
'''1_HelloPython.txt
'''
# ---------------------------------------
# write to the file (UTF-8) is unique to python
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
'''Write me to the file
'''
# ---------------------------------------
# close the file
test_file.close()
# ---------------------------------------
# read from a file. NOTE reading AND writing is "r+"
test_file = open("1_HelloPython.txt", "r+")
# ---------------------------------------
text_in_file = test_file.read()
print(text_in_file)
print("---------------------------------------------------------")
print('\n', "-----------------Class Object----------------------")

# ---------------------------------------
# ---------------------------------------
class Animal:
    name = None  # None is standard python
    height = 0
    weight = 0
    sound = None

    # ---------------------------------------
    # constructor
    # the parameters passed in will auto set to the new class object
    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound
        # ---------------------------------------

    # self is pythons way of saying we will set for a particular object
    def set_name(self, name):  # not self will be auto defined
        self.name = name

    def get_name(self):
        return self.name

    # ---------------------------------------
    def set_weight(self, weight):  # not self will be auto defined
        self.weight = weight

    def get_weight(self):
        return self.weight

    # ---------------------------------------
    def set_height(self, height):  # not self will be auto defined
        self.height = height

    def get_height(self):
        return self.height

    # ---------------------------------------
    def set_sound(self, sound):  # not self will be auto defined
        self.sound = sound

    def get_sound(self):
        return self.sound

    # ---------------------------------------
    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.name, self.height, self.weight,
                                                                      self.sound)


print("We just created a class with a constructor, variables, get/set's and a string to return")
print("We then create an object (Cat) with a standard constructor")
print("Then we print that object using the class print function.")

cat = Animal("Whiskers", 33, 10, "Meow")
print(cat.toString())
'''
Whiskers is 33 cm tall and 10 kilograms and says Meow

'''

print("---------------------------------------------------------")
print('\n', "-----------Inheretance-----------------------------")


class Dog(Animal):
    owner = ""

    # we can create a dog, just like an animal
    # but also can create a dog WITH an owner
    # dog inherets the animal class, but also has an owner
    def __init__(self, name, height, weight, sound, owner):
        self.owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    # We use 'Super' to call the parent Animal class
    # -------------------------------
    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    # -------------------------------
    def get_type(self):
        print("Dog")

    # -------------------------------
    # overwrite functions on super class
    def DtoString(self):
        return "{}, weights {} kilograms, is {}cm tall, he says {}, and his owner is {}".format(self.name,
                                                                                                self.weight,
                                                                                                self.height,
                                                                                                self.sound,
                                                                                                self.owner)


Panzer = Dog('Panzer', 43, 23, 'Bark', 'Nate')
# I CANNOT GET THIS TOSTRING FUNCTION TO OVERWRITE FROM THE PARENT
# print(Panzer.DtoString())
print(Panzer.toString())
print("I can't get the derived class function to overload. Dog should have an owner. ")

print("---------------------------------------------------------")
print("gethere")

print('\n', "----------------POLYMORPHISM-------------------------------")

print('\n', "-----------------------------------------------")

print('\n', "-----------------------------------------------")

print('\n', "-----------------------------------------------")
