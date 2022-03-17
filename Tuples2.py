
print(' Lists vs Tuples')

print(' List Example')
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

print('\n Tuple Example')
perfect_squares = (1, 4, 9, 16, 25, 36)

print('\n Display lengths works for both.')
print('\t # Primes = ', len(prime_numbers))
print('\t # Squares = ', len(perfect_squares))


print('\n Iterate works for both.')
for p in prime_numbers:
    print('\t Prime: ', p)
for n in perfect_squares:
    print('\t Square: ', n)



print('\n\n List Methods: ')
print(dir(prime_numbers))
print(80*'-')


print('\n Tuple Methods: ')
print(dir(perfect_squares))


print('\n The possibilites are similar for both, but lists have more options.')
print(' The tradeoff is that lists take up more memory than tuples. ')


print('\n\n Show the difference using the sys library')
import sys
print(dir(sys))
print('----------------------------------------------------')
print(' Create a list and tuple with the exact same elements.')
list_eg = [1,2,3,'a','b','c', True, 3.14159]
tuple_eg = (1,2,3,'a','b','c', True, 3.14159)
print('\t List Size = ', sys.getsizeof(list_eg))
print('\t Tuple Size = ', sys.getsizeof(tuple_eg))
print(' When you are working with big data sets, this can add up.')


print('\n\n Lists:  You can add, remove, or change data in a list.')
print(' Tuples: Once created, they cannot be changed later in the program.')


print('\n\n Lists:  Relatively it takes more time to make lists than tuples')
print('  Using another import to time the program.')
print('   We create a 5 element list, and a 5 element tuple each 1 million times.')
print('   We measure the time that it takes to make 1 million of each.')
import timeit
list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number = 1000000)
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number = 1000000)

print(" List Time = ", list_test)
print(" Tuple Time = ", tuple_test)




empty_tuple = ()
test1 = ('a')
test2 = ('a', 'b')
test3 = ('a', 'b', 'c')
print('\n\n', empty_tuple)
print(test1)
print(test2)
print(test3)
print(' NOTE: A tuple with only 1 element still needs a comma after that element.')
test1 = ('a',)
print(test1)
print(' Or else it auto turns into a list. ')




print('\n\n Alternative construction to tuples.')
test1 = 1,
test2 = 1,2
test3 = 1,2,3
print(test1)
print(test2)
print(test3)
print(type(test1))
print(type(test2))
print(type(test3))



print('\n\n Tuples can work with indices and by comma seperation.')
print(' Checking: age, country, knows_python')
person1 = (27, 'Vietnam', True)
print(' Using indices:  ')
age = person1[0]
country = person1[1]
knows_python = person1[2]
print('\t Age = ', age)
print('\t Country = ', country)
print('\t Knows Python = ', knows_python)
print('---------------------------')
person2 = (21, 'Switzerland', False)
print(' Using comma seperation: ')
age, country, knows_python = person2
print('\t Age = ', age)
print('\t Country = ', country)
print('\t Knows Python = ', knows_python)

print('\t\t You get the same results. This is why you need a comma with just one element.')



print('\n\n Simple Example')
simple_tuple = (1, 2, 3)
x,y,z = simple_tuple
print(x)
print(y)
print(z)
