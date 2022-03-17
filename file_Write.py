
newline = "\n------------------"
print(newline)



print("Start by reading a local file")
notes_file = open("employees.txt", "r+")
print(notes_file.read())
notes_file.close()

# =============================
print(newline)
print("We want to add a new employee to the file. - Append")
notes_file = open("employees.txt", "a")
notes_file.write("\nStanley - Salesman")


# If we open with just "a" or "w" technically we can't read it.
# You will get an error if you use the read function, but don't have "r"
notes_file = open("employees.txt", "r")
print(notes_file.read())
notes_file.close()

# =============================
print(newline)
print("Create a new file")
print("This will overwrite/redo that file each time you run this again.")
notes_file = open("newfile.txt", "w")
notes_file.write("Put this in the new file.")
notes_file.close()

