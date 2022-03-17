

print(' Sets are to help organize data.')

example = set()
print(dir(example))

print('\n\n The set is to hold anything.')
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")
print(example)


print('\n\n A set, the order does not matter. It may appear in different ways.')
print(' Sets will not contain duplicates.')
print(' If I add   42   the set will not change. There is a 42 there already.')


print('\n Make a simple removal with    remove. Will get an error if the element is not there.')
#   example.remove(50)
example.remove(42)
print(example)


print('\n\n Second way to remove an element. Discard, will not give an error if it is not there.')
print(' This is good if you do not need to know the error. ')
example.discard(50)


print('\n\n Second way to create and pre=populate a set. You need brackets.')
example2 = set([28, True, 2.17234, 'Carbon'])
print('\t', example2)


print('\n\n See the length of a set. ')
print('\t', len(example2))


print('\n\n You can create a union and combine the sets.')
odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])
print(' odds = ', odds)
print(' evens = ', evens)
print('\t odds.union(even) = ', odds.union(evens))

print('\n odds = ', odds)
print(' primes = ', primes)
print(' odds.intersection(primes) = ', odds.intersection(primes))



print('\n\n See if an element exists in a set.')
print('2 in primes\t', 2 in primes)
print('9 in evens\t', 9 in evens)




