

# Functions
print('')
print('\n111 A simple function using one parameter')
def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print("\t%d squared is %d." % (n, squared))
    return squared


# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)
square(6)


# =================================================
print('\n\n222 A function using two parameters.')
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print("\t%d to the power of %d is %d." % (base, exponent, result))

power(37,4)  # Add your arguments here!



# =================================================
print('\n333) Two functions, one that uses the other.')
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    n = one_good_turn(n)
    return n + 2

doubleVal = deserves_another(6)
print('\t', doubleVal)



# =================================================
print('\n\n444) Two functions, one used if/else and the other function.')
def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


print('\t',by_three(9))




# =================================================
print('\n\n Some math functions need an import, such as sqrt')
import math
print('\tThe sqrt of 25 = ', math.sqrt(25))
print('\n Note we can do the import without having to do import math and')
print(' use math.sqrt(). ')
print('\t from math import sqrt     just to get sqrt')

from math import sqrt
print('sqrt of 36 is = ', sqrt(36))

print('\n from math import *')
from math import *
print('The import * will import everything from that library.')
print(dir(math))
print('Now we can use cos() straight since we imported everything from math.')
print(cos(3.14159))




print('\n\n\n Pointer to a list so we can send a list to a function.')
print('These are built in functions to python. Don\'t need to import.')

def biggest_number(*args):
    print('print(max(args))')
    print('\t',max(args))
    return max(args)


def smallest_number(*args):
    print('print(min(args))')
    print('\t',min(args))
    return min(args)


def distance_from_zero(arg):
    print('Note: the abs() only takes one number. Not a list.')
    print('print(abs(arg))')
    print('\t',abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


# Set maximum to the max value of any set of numbers on line 3!
maximum = max(3,6,23,43,2234,5,345,25,457,786,546)
print('\n\t max in list = ', maximum)



# =================================================
print('\n\n To see the specific data type of a variable you have.')
print('\t type(variable)    =')
x = 34
print(type(x))
y = 3.145324
print(type(y))
z = 'asdf'
print(type(z))



# =================================================
print('\n\n Simple function using if/elif/else and variable types.')
x = input('Enter a number   ')
def distance_from_zero(x):
    if type(x) == int:
        return abs(x)
    elif type(x) == float:
        return abs(x)
    else:
        return 'Nope'

print('\t',distance_from_zero(x))
print('Remember that an input automatically converts to a string if you don\'t say otherwise.')
