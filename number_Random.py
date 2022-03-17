

print('\n Python has a random module built in.')
print(' You need to import random')
import random
print(dir(random))

print('\n This is the explanation of random. \n========================')
print(help(random.random))
print('\t Note, on the print. [ means it can return 0, but ) means it cant return 1')
print('=============================')



print('\n\n Display 10 random numbers from interval [0, 1)')
for i in range(10):
    print(random.random())




print('\n\n Generate random numbers from interval [3, 7)')
print(' First create a function to get a base random number + 3')
print(' Function. Num is <1 hten *4, so will be <4, then + 3')
def my_random():
    return 4 * random.random() + 3

for i in range(10):
    print(my_random())



print('\n\n Easy built in function for randoms in a range.')
for i in range(10):
    print(random.uniform(5, 100))



print('\n\n Get a random number around a mean, with a standard deviation.')
print(' This will give us a set mostly around 5. Change the second for accuracy to 5')
for i in range(10):
    print(random.normalvariate(5, 0))
print('-----------------')
for i in range(10):
    print(random.normalvariate(5, 1))



print('\n\n Simulate the roll of a die. Ex get a whole number')
for i in range(10):
    print(random.randint(1,6))



print('\n\n Random (Rock  Paper  Scissors.')
print(' Use the specific random function (choice), and pass in a list of values to choose from.')
outcomes = ['rock', 'paper', 'scissors']
for i in range(10):
    print(random.choice(outcomes))



