

newline = "\n-----------------"
print(newline)

print("Create function that says hi to a user.")
#
def say_hi():
    print("Hello sent user")


print(newline)
print("Call the function")
say_hi()



# ------------------------------
print(newline)
print("Pass in parameters")
def say_hi(name):
    print("Hello " + name)

#--------------
say_hi("Nate")
say_hi("Patricks")


# ------------------------------
print(newline)
print("Pass in 2 parameters")
def say_hi(name1, name2):
    print("Hello " + name1 + " and " + name2)

say_hi("Nate", "Patrick")


# ---------------------------
print(newline)
print("Pass in a string and an int.")
print("")
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Nate", 33)

# ======================================
print(newline)
print("Funtion with a return function")
def cube(num):
    value = pow(num, 3)
    return value

cubeofThree = cube(3)

print("cube(3) = " + str(cubeofThree))