

# "Read a file called file_read.txt"

# open("file_read.txt", "r")    # r - only want to read file
# open("file_read.txt", "w")    # w - write file
# open("file_read.txt", "a")    # a - append to file
# open("file_read.txt", "r+")   # r+ - read and write file

notes_file = open("file_read.txt", "r")  # r - only want to read file
# When you are done with a file, make sure to close it also.
notes_file.close()


notes_file = open("file_read.txt", "r")  # r - only want to read file
# "Check if a file is readable"
print(f'\nnotes_file.readable() = {notes_file.readable()}')

# "Actually read/print the contents of the file."
print(f'notes_file.read() = \n{notes_file.read()}')
notes_file.close()


# "Open file, and read specific lines"
notes_file = open("file_read.txt", "r")
# Readline remembers what line.
# Multiple uses will auto move onto next line.
print(f'\nnotes_file.readline() = {notes_file.readline()}')
print(f'notes_file.readline() = {notes_file.readline()}')
print(f'notes_file.readline() = {notes_file.readline()}')
notes_file.close()


notes_file = open("file_read.txt", "r")
# "Plural readlines, goes through, and places each/every line into a local array also."
print(f'notes_file.readlines() = {notes_file.readlines()}')
notes_file.close()
