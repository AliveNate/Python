# Create a list
li = [9,1,8,2,7,3,6,4,5]


print('\n\nPrint out the original list.')
print('Original List:\t', li)


# Make new variable
print('\n\nWe need to make a new variable, and use the built in sort function.')
s_li = sorted(li)
print('Sorted List:\t', s_li)


print('\n\nWe can also sort without a new variable using:   li.sort()')
li.sort()
print('The original list after a specific sort:', li)
print('Note: the sort() function returns nothing, it just changes the original.')
print('Cannot use   s_li = li.sort()    because .sort() doesnt return anything.')


# ==============================================================
print('\n\nTo reverse the order of a sorted list.')
s_li = sorted(li, reverse = True)
print(s_li)