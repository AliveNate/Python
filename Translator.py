

newline = "\n---------------"


print(newline)

print("We need to create a translate language")
print("Normal english, but all vowels turn into g")


def translate():
    phrase = input("Please give us a phrase: ")
    translation = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            translation = translation + "g"

        else:
            translation = translation + letter

    return translation


print(newline)
print(translate())