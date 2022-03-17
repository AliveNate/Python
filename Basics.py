
newline = "\n-------------------"
print('')

# ===================================
name = "Jennifer"
print(name[:])      # Print beginning to end
print(name[0:])     # Print first char to end
print(name[1:-1])   # Print 2nd char to end -1 char [ ennife ]
# ===================================
# ===================================
print(newline)
# ===================================
print("Formatted strings" + newline)
first = "John"
last = "Smith"
message = first + " fucking " + last + " is a coder."
print(message)
msg = f'{first} fucking {last} is a coder' # Formatted message, more efficient.
print(msg)
# ==================================
print(newline)
print("Basic String Stuff ")
print("Show the length of the string.")
print(message)
print("Length = " + str(len(message)))
print("Uppercase = " + str(message.upper()))
print("Lowercase = " + str(message.lower()))
print("Find the first \'f\' = "  + str(message.find("f")))
print("Replace the  f  with Z = " + str(message.replace("f", "Z")))
print("Is  fucking  in the message = " + str("fucking" in message)) # case sensitive
# ===================================
# ===================================
print(newline)
print("Basic Number Stuff")
print("10 + 3 = " + str(10 + 3))
print("10 - 3 = " + str(10 - 3))
print("10 * 3 = " + str(10 * 3))
print("10 / 3 = " + str(10 / 3))
print("10 % 3 = " + str(10 % 3))
x = 10
x = x + 3
print("x = " + str(x))
print("4^3 = " + str(4 ** 3))
print("Round 2.9 = " + str(round(2.9)))
print("Import the math module")
import math
print("Floor of 2.9 = " + str(math.floor(2.9)))
print("Google - python 3 math module. Many functions.")
# ===================================
# ===================================
print(newline)
print("Conditional Operators")
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:     #implies if they are BOTh True
    print("Eligible for loan.")
# -------------------------------------
if has_high_income or has_good_credit:     #implies if they one is True
    print("Eligible for loan.")
# -------------------------------------
if has_high_income and not has_good_credit:     #implies if they one is True and one is false
    print("Eligible for loan.")
# ===================================
# ===================================
print(newline)
print("Weight Converter")
weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} kilograms.')
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f'You are {converted} pounds.')

# ===================================
# ===================================
print(newline)
print("Secret Number While Loop")
secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:    #Run while we havent reached the limit
    guess = int(input("Guess a number: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("While loop executed to completion. You made 3 incorrect guesses.")

# ===================================
# ===================================
print(newline)
message = input("What is your message >")   # user input any message
words = message.split(" ")                  # Split user message at spaces, put in array
emojis = {                                  # Ex. Message =     "I am really happy :)" --> input smiley face.
    ":)": "😀",                              # Mac --> edit --> emojis and symbols
    ":(": "🥺"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)  # i am really happy 😀
# ===================================
