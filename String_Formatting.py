import sys
import os

Jenn = {'name': 'Jenn', 'age': 23}
Nate = {'name': 'Nate', 'age': 30}
person = {'name': 'Ben', 'age': 24}

# 1 This will just take the person based on the specific traits that are given to the person.
sentence = 'My name is ' + Jenn['name'] + ' and I am ' + str(Jenn['age']) + ' years old.'
print('1) Use object specifics -->             ', sentence)

# 2 This will give the same sentence. The {} will take the those listed in order.
sentence2 = 'My name is {} and I am {} years old.'.format(Jenn['name'], Jenn['age'])
print('2) Use order of placement -->           ', sentence2)

# 3 This will give the but you can pull listed traits out of order if need be.
sentence3 = 'My name is {1} and I am {0} years old.'.format(Jenn['age'], Jenn['name'])
print('3) Use any location from assignment --> ', sentence3)


# 4 This sentence will just the place and the traits from two different. List position/trait.
sentence4 = 'My name is {0[name]} and his age is {1[age]}'.format(Jenn, Nate)
print('4) Use 2 different whole objects -->    ', sentence4)


# 5 You can specify based on internal assignment values, based on name..
sentence5 = 'My name is {name} and I am {age} years old.'.format(age = '30', name = 'Jenn' )
print('5) Use internal assignment values based on name -->   ', sentence5)


# 6 The same can be done with a list instead of a vector.
jennList = ['Jenn', 23]
sentenceList = 'My name is {0[0]} and I am {0[1]} years old.'.format(jennList)
print('6) Use a list -->                       ', sentenceList)


# ===============================================================
# ============================Class=====================================================
# Create a class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object from the person class
person1 = Person('Jack', '31')
# Create a string using object attributes
sentenceClass = 'My name is {0.name} and I am {0.age} years old.'.format(person1)
print('\n\n This is from a class object --> ', sentenceClass)

# ============================Class=====================================================
# ===============================================================



print('\n\n')
tag = 'hi'
text = 'This is a headline'

sentence7 = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence7)


# ===============================================================
# ===============================================================
S = 'Spam'
print('\n\nThe string S = ', S)
print('The string S length is len(S) = ', len(S))
print('The first char in the string S is S[0] = ', S[0])
print('The second char in the string S is S[1] = ', S[1])
print('Python can also work from the back of a string.')
print('The last char in S is S[-1] = ', S[-1])
print('The second to last char in S is S[-2] = ', S[-2])
print('The 1:3 chars in the string S. Note S[1:3] only gets char1 and char2 = ', S[1:3])
# ===============================================================
# ===============================================================


# ===============================================================
# ===============================================================
print('\n\n')
# This will print values 1 - 10 same as: (for(int i=1; i<11; i++)
for i in range(1,11):
    sentence8 = 'The value is {}'.format(i)
    print(sentence8)

# Same thing but we want to automatically pad 2digits  so 2 will be 02
print('---------------')
# Include :02 in the {} to say we want TWO digits guaranteed.
for i in range(1,11):
    sentence8 = 'The value is {:02}'.format(i)
    print(sentence8)

# Same thing but we want to automatically pad 3digits  so 2 will be 002
print('---------------')
# Include :03 in the {} to say we want THREE digits guaranteed.
for i in range(1,11):
    sentence8 = 'The value is {:03}'.format(i)
    print(sentence8)
# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================
print('\n\n')
print('How to print out a specific number of decimal places.')
pi = 3.14159265
sentencePi = 'Pi is equal to {:.3f}'.format(pi)
print(sentencePi)
sentencePi = 'Pi is equal to {:.6f}'.format(pi)
print(sentencePi)
# ===============================================================
# ===============================================================


# ===============================================================
# ===============================================================
# Print out a large number with comma seperators
print('\n\n')

print('A number using a comma to seperate the digits at a location.')
sentenceSeperate = '1MB is equal to {:,} bytes'.format(1000**2)
print(sentenceSeperate)
print('---------------')
print('A number using a comma to seperate the digits at a location, and add decimal distinction.')
sentenceSeperate = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentenceSeperate)
# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================
# Printing out and formatting dates and times.
print('\n\n')
# Datetime library
# https://docs.python.org/3/library/datetime.html

# we need another library
import datetime

print('auto format (year, month, day, hour, minute, second)')
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
print('---------------')

# Now using specific date format from library above.
print('# Now using specific date format from library above.')
sentence_Date = '{:%B %d %Y}'.format(my_date)
print(sentence_Date)
print('---------------')

# Now we will use libary abbrev. %A and %J for day of the
print('We want the date in format, and specifics about that date. ')
print('Complicated. We are only passing in one reference [my_date] but we have 3 brackets.')
print('In each bracket we need a 0 to reference [my_date] the object passed in.')
print('%B %d %Y %A %j are all inherent library abbreviations. Found on webpage above')
print('EX. %A will reference the library and know that the date was a Saturday.')
print('---------------')
sentence_Date2 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence_Date2)
# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================