newline = "\n==================="
# ===========================
print(newline + "Trick 4") # ============
print("Enumerator count")
names = ['Corey', 'Chris', 'Dave', 'Travis']
# Normal:
# Start with index, and increase each loop.
# index=0  --> index += 1      Works but is sloppy
# Better:
for index, name in enumerate(names, start=1):
    print(index, name)
'''
1 Corey
2 Chris
3 Dave
4 Travis
'''

# ===========================