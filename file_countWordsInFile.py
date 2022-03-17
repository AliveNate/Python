
newline = "\n----------"
# ===========================
print(newline + "Trick 3") # ============
print("Context Managers - Google for more info")
print("Function open/close files.")
# Normal
# fyle = open('TRICKS.txt', 'r')
# file_contents = fyle.read()
# fyle.close()
# -------------------------
# Faster Function
# Opens file, then auto-closes after loop.
with open("TRICKS.txt", 'r') as f:
    file_contents = f.read()


words = file_contents.split(' ')
word_count = len(words)
print(f'Word count = {word_count}')

# ===========================
# ===========================