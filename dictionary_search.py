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
    age = 'Unkown'
print('Dick is %s years old.' % age)

print('\n---------------')
# The good way
age = ages.get('Dick', 'Unkown')
print('Dick is %s years old.' % age)
print('This one line, will find and get age for Dick, but if not there, falls back to Unknown')
print('Same thing, but more efficient.')
