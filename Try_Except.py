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
