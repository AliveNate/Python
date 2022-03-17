newline = "\n---------------"
print(newline + "Trick 1") # ============
print("You can use underscores in numbers, in place of commas."
      "\nThis will not affect an integer:  10_000_000_000")

n1 = 10_000_000_000
n2 = 1_000_000
print(f'10_000_000_000 '
      f'\n+    1_000_000 \nTotal = {n1 + n2}')
print(f'\nAND you can add commas to print:')
print("\'{Total:,}\' = ")
print(f'{(n1 + n2):,}')
'''
10_000_000_000 
+    1_000_000 
Total = 10001000000

AND you can add commas to print:
'{Total:,}' = 
10,001,000,000

'''
# ===========================