

print('\n\n This is a while loop that will operate if we keep numbers coming in.')
print(' This will run until you type  stop  ')
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    elif reply.isnumeric():
        print('\t That was a number.')
        print(int(reply) ** 2)
    else:
        print('\t That was NOT a number.')
print('Bye')



print('\n\n')
condition = 1

while condition < 10:
    print(condition)
    condition += 1
print(' While loop will print and add 1 to condition until 10')



print('\n\n Asks if it is true or false, this will print doing stuff forever.')
#   while True:
    #   print('doing stuff')
    #   pass


print('\n\n This only catches neg vs pos ints.')
print(' Rememeber, input is inherently a string.')
num = -1
while num < 0:
    num = int(input('Give me a positive number: '))

