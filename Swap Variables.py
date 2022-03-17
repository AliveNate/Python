print('\n\ntip 3===========================================================')
print(' We want to swap two variables')
x = 10
y = -10
print("Before: x = %d, y = %d" % (x, y))
# The bad way
tmp = y
y = x
x = tmp
print("After: x = %d, y = %d" % (x, y))
print('\n---------------')
# That took 3 lines
print('x, y\t', x, y)
x, y = y, x
print('x, y\t', x, y)
print('Python allows for a quick, simple switch without a tmp_var')
