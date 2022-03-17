
#!/usr/bin/env python

'''This program was developed by Nate Terry
This has the user guess a number between 1 and 100.
This is targeted at the worflow of the program.'''

def main():
    # Initialize the program.
    # randomNumber = 35   # randomNumber set just to have a base.
    import random
    randomNumber = random.randint(1,100)

    found = False       # Flag variable to see if guessed.
    # found will be False until random matches user guess.
    print('Run through the guessing process.')

    while not found:
        userGuess = int(input("Guess a number between 1 and 100: "))

        if userGuess == randomNumber:
            print("\tYou got it!")
            found = True
        elif userGuess > randomNumber:
            print('\tGuess lower.')
        elif userGuess < randomNumber:
            print('\tGuess higher.')
        else:
            print('\tThat\'s not it.')
    print('Thanks for playing our game. ')





if __name__ == "__main__":
    main()
