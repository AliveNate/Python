print('\n\ntip 1===========================================================')
print('  Tip 1 - How to most efficiently get the list and details. ')
cities = ['Marseille', 'Amnsterdam', 'New York', 'London']
i= 0
for city in cities:
    print(i, city)
    i += 1

print('\t This works but is not efficient. Now the good way...')
print('---------------')
for i, city in enumerate(cities):
    print(i, city)
print('\t They do the same thing, but enumerate is simple for walking through a list.')
