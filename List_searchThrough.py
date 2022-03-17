print('\n\ntip 5===========================================================')
print('For loops. We want to search a list to see if something is in there.')
needle = 'd'
haystack = ['a','b','c']
# The bad way
found  = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not Found')

print('\n---------------')
# The good way
found  = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else:
    print('Not Found')
print('Very simple and nearly the same thing, but we lose lines, due to else statement.')
