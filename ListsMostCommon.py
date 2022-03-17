# Basic List
# NCT - there are numerous examples how to create/format/use lists.
#       These are just basic examples to potential future use.
# These list elements are all of the same type
zoo = ['bear', 'lion', 'panda', 'zebra']
print(zoo)
# -----------------------------------
# But these list elements are not
biggerZoo = ['bear', 'lion', 'panda', 'zebra', ['chimpanzees', 'gorillas', 'orangutans', 'gibbons']]
print(biggerZoo)
# -----------------------------------
"""Lists Versus Tuples
Tuples are used to collect an immutable ordered list of elements. This means that:

    You can’t add elements to a tuple. There’s no append() or extend() method for tuples,
    You can’t remove elements from a tuple. Tuples have no remove() or pop() method,
    You can find elements in a tuple since this doesn’t change the tuple.
    You can also use the in operator to check if an element exists in the tuple.

So, if you’re defining a constant set of values and all you’re going to do with it is iterate through it, 
    use a tuple instead of a list. It will be faster than working with lists and also safer, as the tuples 
    contain “write-protect” data.   """
"""
Lists Versus Dictionaries

    A list stores an ordered collection of items, so it keeps some order. Dictionaries don’t have any order.
    Dictionaries are known to associate each key with a value, while lists just contain values.


Use a dictionary when you have an unordered set of unique keys that map to values.
Note that, because you have keys and values that link to each other, the performance will be better 
    than lists in cases where you’re checking membership of an element.
"""
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n1. How To Randomly Select An Element In A List")
# Import `randrange` from the `random` library
from random import randrange

# Construct your `randomLetters` variable with a list of the first 4 letters of the alphabet
randomLetters = ['a', 'b', 'c', 'd']

# Select a random index from 'randomLetters`
randomIndex = randrange(0,len(randomLetters))

# Print your random element from `random`
print(randomLetters[randomIndex])

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n2. How To Convert A List To A String")
# List of Strings to a String
listOfStrings = ['One', 'Two', 'Three']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)

# List Of Integers to a String
listOfNumbers = [1, 2, 3]
strOfNumbers = ''.join(str(n) for n in listOfNumbers)
print(strOfNumbers)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n2.5 Transform a list to either a set or tuple")
# Pass your list to `tuple()`
tuple(listOfStrings)

# Transform your list into a set
set(listOfStrings)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n3. How To Convert Lists To A Dictionaries")
# You will need to make sure that ‘hello’ and ‘world’ and ‘1’ and ‘2’ are interpreted as key-value pairs.
#       The way to do this is to select them with the slice notation and pass them to zip().
helloWorld = ['hello','world','1','2']
list(zip(helloWorld))
# You will pass this to the dict() function, which will interpret hello as a key and world as a value.
#       Similarly, 1 will be interpreted as a key and 2 as a value.
# Convert to a dictionary
helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result
print(helloWorldDictionary)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n4. How To Determine The Size Of Your List in Python.")
# Pass `justAList` to `len()`
justAList = [1,2,3,4,5,6]
len(justAList)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n5. The Python append() and extend() Methods?")
# Append [4,5] to `shortList`
shortList = [1,2,3]
shortList.append([4, 5])

# Use the `print()` method to show `shortList`
print(shortList)

# Extend `longerList` with [4,5]
longerList = [1,2,3]
longerList.extend([4, 5])

# Use the `print()` method to see `longerList`
print(longerList)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n6. How To Concatenate Lists in Python")
# Concatenate `shortList` with `[4,5]`
plusList = shortList + [4,5]

# Use the `print()` method to see `plusList`
print(plusList)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n7. How To Sort a List in Python")
# The sorted() function can be applied to any Iterable object, which means that
#   it also accepts strings, sets, dictionaries when they are passed to it!
# Use `sort()` on the `rooms` list
rooms = ["g209", "e204", "a203", "b302"]
rooms.sort()

# Print out `rooms` to see the result
print(rooms)

# Now use the `sorted()` function on the `orders` list
orders = ["kcaoibew32ion", "93dhf8fh32", "n283h8fd", "238hfiu2"]
sorted(orders)

# Print out orders
print(orders)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n8. How To Clone Or Copy A List in Python")
# Copy the grocery list by slicing and store it in the `newGroceries` variable
groceries = ["apple", "orange", "broccoli", "chicken"]
newGroceries = groceries[:]
# Copy the grocery list with the `list()` function and store it in a `groceriesForFriends` variable
groceriesForFriends = list(groceries)
# Import the copy library
import copy as c
# Create a `groceriesForFamily` variable and assign the copied grocery list to it
groceriesForFamily = c.copy(groceries)
# Use `deepcopy()` and assign the copied list to a `groceriesForKids` variable
groceriesForKids = c.deepcopy(groceries)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n9. List comprehension - create list based on math equation.")
mathlist = [x**2 for x in range(10)]
print(mathlist)

# Let’s say you want to make the same list as before, but you only want to multiply the
#   numbers that can be divided by 2. Even this is easy with the help of list comprehension:
mathlist = [x**2 for x in range(10) if x%2==0]
print(mathlist)

print("Transform your lists into other lists")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mathlist = [(lambda x: x*x)(x) for x in myList]
print(mathlist)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n10. Counting the occurrences of one item in a list")
# Count the occurrences of the number 4
print([1, 2, 9, 4, 5, 4, 1].count(4))

# Count the occurrences of the letter "a"
list = ["d", "a", "t", "a", "c", "a", "m", "p"]
print(list.count("a"))

print("Counting all items in a list with count()")
list= ["a","b","b"]
setcount = [[x,list.count(x)] for x in set(list)]
print(setcount)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n11. How To Split A Python List Into Evenly Sized Chunks")
# Your list `x`
x = [1,2,3,4,5,6,7,8,9]

# Split `x` up in chunks of 3
y = zip(*[iter(x)]*3)
del list  # We redefined list as zip, and now need to remove list
# Use `list()` to print the result of `zip()`
print(list(y))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n11.2 How To Split A Python List Into Evenly Sized Chunks")
# Method to split up your lists into chunks
def chunks(list, chunkSize):
    """Yield successive chunkSize-sized chunks from list."""
    for i in range(0, len(list), chunkSize):
        yield list[i:i + chunkSize]

# Use your `chunks` function to print out chunks of the same size
import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n11.3 How To Split A Python List Into Evenly Sized Chunks")
# Set up your list and chunk size
list = range(0, 50)
chunk = 5

# Split up your list into chunks
print([list[i:i + chunk] for i in range(0, len(list), chunk)])

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n12. How To Loop over A List in Python")
# This is your list
mylist = [[1,2,3],[4,5,6,7],[8,9,10]]

# Loop over your list and print all elements that are of size 3
for x in mylist:
      if len(x)==3:
        print(x)

print("-----------------------")
# This is your list
myList = [3,4,5,6]

# Loop over `myList` and print tuples of all indices and values
for i, val in enumerate(myList):
     print(i, val)


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n13. How To Create Flat Lists Out Of Lists")
# Your initial list of lists
list = [[1,2],[3,4],[5,6]]

# Flatten out your original list of lists with `sum()`
flatlist = sum(list, [])
print(flatlist)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n15. How To Remove Duplicates From A List in Python")
# Your list with duplicate values
duplicates = [1, 2, 3, 1, 2, 5, 6, 7, 8]

# Print the unique `duplicates` list
print((set(duplicates)))

# A list with small numbers
smallNumbers = [1, 2, 3]

# Print the unique `duplicates` list without the small numbers
print(set(duplicates) - set(smallNumbers))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

"""
In general, there seem to be four reasons why Python programmers prefer NumPy arrays over lists in Python:
    because NumPy arrays are more compact than lists.
    because access in reading and writing items is faster with NumPy.
    because NumPy can be more convenient to work with, thanks to the fact that you get a lot of vector and matrix operations for free
    because NumPy can be more efficient to work with because they are implemented more efficiently.
"""
###NCT had issues with this.
# print("\n17. How To Create Empty NumPy Arrays")
# import numpy
# numpy.array([])
# # Make a NumPy array of four rows and two columns and filled with 0
# numpy.zeros(shape=(4,2))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

print("\n18. How To Do Math With Lists in Python")
cost = [0.424, 0.4221, 0.4185, 0.4132, 0.413]
cases = [10, 20, 30, 40, 50]
# You can easily calculate the weighted average with the following pieces of code:
for c in range(len(cost)):
   cost[c] = (cost[c] * cases[c] / sum(cases))
cost = sum(cost)
print(cost)