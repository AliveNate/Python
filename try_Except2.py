


newline = "\n-----------------"

print("We don't want to crash a program just by an incorrect input.")

try:
    value = 10 / 0 # Cant divide by zero
    number = int(input("Enter a number: "))
    print(number)


# We can create our own exceptions, but, It is best to uses python set errors when possible.
except ZeroDivisionError:
    print("Divided by zero")

except ValueError:
    print("Invalid input")