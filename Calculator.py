import sys
import os

print("\n--------------------------------------------------")
print("The Calculator function")
#function as a calculator
def add(num1, num2):
    print(num1, ' + ', num2, ' = ', num1 + num2)
    return num1 + num2

def sub(num1, num2):
    print(num1, ' - ', num2, ' = ', num1 - num2)
    return num1 - num2

def mul(num1, num2):
    print(num1, ' * ', num2, ' = ', num1 * num2)
    return num1 * num2

def div(num1, num2):
    print(num1, ' / ', num2, ' = ', num1 / num2)
    return num1 / num2


#create a main function area
def mainx():
    operation = ''
    while operation != 'stop' and operation != 'Stop' and operation != 'STOP':
        operation = input("What do you want to do: ( + - * / ): \n\t(Type 'stop' to exit) ")
        if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
            print("You did not enter a valid response")
        else:
            #Remember we need an int before this input line to clarify a number
            num1 = int(input("Enter num1:  "))
            num2 = int(input("Enter num2:  "))
            if (operation == '+'):
                add(num1, num2)
            elif(operation == '-'):
                (sub(num1, num2))
                (sub(num2, num1))
            elif(operation == '*'):
                (mul(num1, num2))
            elif(operation == '/'):
                (div(num1, num2))
                (div(num2, num1))
        print('----------------------------')


mainx()