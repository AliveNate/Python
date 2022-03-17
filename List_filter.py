
# 4.2. Filter
# As the name suggests, filter creates a list of elements for which a
#   function returns true. Here is a short and concise example:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

# The filter resembles a for loop but it is a builtin function and faster.
