newline = "\n---------------"

# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 2") # ============
print("Change if/else condition into 1 line")
condition = True
# Normal Setup
if condition:
    x = 1
else:
    x = 0
# -----------------------
# Single line
# X=1 if condition is true, else x=0
x = 1 if condition else 0
print(f'x = {x}')
# ===========================