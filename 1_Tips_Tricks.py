

print('\n\ntip 3===========================================================')
print(' We want to swap two variables')
x = 10
y = -10
print("Before: x = %d, y = %d" % (x, y))
# The bad way
tmp = y
y = x
x = tmp
print("After: x = %d, y = %d" % (x, y))
print('\n---------------')
# That took 3 lines
print('x, y\t', x, y)
x, y = y, x
print('x, y\t', x, y)
print('Python allows for a quick, simple switch without a tmp_var')



print('\n\ntip 4===========================================================')
print('Dictionaries. Get the value of an unknown key')
ages = {
    'Mary': 31,
    'Jonathon': 28
}
print(" age = ages['Dick'] will not work. No 'Dick' in dictionary. ")
# the bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
print('Dick is %s years old.' % age)

print('\n---------------')
# The good way
age = ages.get('Dick', 'Unkown')
print('Dick is %s years old.' % age)
print('This one line, will find and get age for Dick, but if not there, falls back to Unknown')
print('Same thing, but more efficient.')



print('\n\ntip 5===========================================================')
print('For loops. We want to search a list to see if something is in there.')
needle = 'd'
haystack = ['a', 'b', 'c']
# The bad way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not Found')

print('\n---------------')
# The food way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else:
    print('Not Found')
print('Very simple and nearly the same thing, but we lose lines, due to else statement.')



print('\n\ntip 6===========================================================')
print(' This will read in a txt file and read lines one by one.')
f = open('1_Tips_Tricks.txt')
text = f.read()
for line in text.split('\n'):
    print('\t', line)
f.close()

print('\n---------------')
with open('Tips_Tricks.txt') as f:
    for line in f:
        print(line)



print('\n\ntip 7===========================================================')
print('')
print('Converting')
print(int('1'))
print('Done!')

print('\n---------------')
print(' This is simple, but wont work if it isnt a number.')
print(' print(int("x"))   wont work. Use a try/except')

print('Converting')
try:
    print(int('x'))
except:
    print('Conversion Failed')
else:
    print('Conversion Successful.')
print('Done!')



print('\n\n===========================================================')
print('')
