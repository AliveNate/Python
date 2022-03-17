

name = input('Enter Name')
print(name)


print('\n The input automatically uses the input as a string. ')
print(' We have to convert it to a number or anything else we need to use.')

age = input('What is your age?')
print('\tage*2 will just be the number twice = \t', age*2)
print('\tWe need to convert: int(age)*2 = \t', int(age)*2)



print('\n\n This is a while loop that will operate if we keep numbers coming in.')
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    print(int(reply) **2)
print('Bye')