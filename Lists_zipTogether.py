
print('\n\ntip 2===========================================================')
print(' Lists: walk through two lists at the same time.')
x_list = [1,2,3]
y_list = [2,4,6]
# The bad way:
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x,y)



print('\n------The Good Efficient way: Use zip---------')
# The good way to go through two lists at the same time
for x,y in zip(x_list, y_list):
    print(x,y)
