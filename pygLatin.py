

'''Remember strings are immutable, you cannot change an existing string.
You must create a list copy to  to change.'''


def pygLatin():
    user_word = input("Please enter a word: ")
    list_change = list(user_word) #turn input word into a char list
    temp = user_word[0]
    length = len(user_word)
    for i in range(0, length):
        if i == (length - 1):
            list_change[i] = temp
        else:
            list_change[i] = list_change[i + 1]


    new_word = "".join(list_change)
    new_word = new_word + 'ay'
    print(new_word)



pygLatin()



# OR
# Both are pig latin, but different formats.


pyg = 'ay'

original = str(input('Enter a word:'))

if len(original) > 0 and original.isalpha():
    print(original)
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]
    print(new_word)
else:
    print('empty')