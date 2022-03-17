

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")
# ---------------------------------------
print("\n\nWe know that in the 2nd sentence in the poem, our input is the first word, "
      "\nand we want to make sure that the first letter is uppercase:")
plural_noun = plural_noun[0].upper() + plural_noun[1:]

# --------------------
print("\n\n")
print("Roses are " + color + ".")
print(plural_noun + " are blue.")
print("I love " + celebrity + ".")