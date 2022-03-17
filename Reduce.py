
# 4.3. Reduce

# Reduce is a really useful function for performing some computation on a
#   list and returning the result. It applies a rolling computation to sequential
#   pairs of values in a list. For example, if you wanted to compute the product
#   of a list of integers.

# So the normal way you might go about doing this task in python is using a basic for loop:

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24

# Now let’s try it with reduce:

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24

