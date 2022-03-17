import sys
import os

print('\n Slicing is how to extract certain elements from a list or a string.')


my_list =       [  0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Index         [  0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Neg. Index    [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
print('\t Print my list: \t', my_list)


print('\n\n We can print a string or list based on char index either front or back')
print('\t my_list[4]  =\t', my_list[4])
print('\t my_list[-4] =\t', my_list[-4])


print('\n\n We can also access a certain range in the string or list.')
print('\t my_list[0:5] =\t', my_list[0:5])
print(' Remember that we are grabbing up until 5 --> so we get 0 -> 4')


print('\n\n We cannot state that we want to print the end char in a list using the colon.')
print(' Remeber that it goes up UNTIL that. So use an empty colon.')
print('\t my_list[1:] =\t', my_list[1:])


print('\n\n We can also increment based on steps. Add another colon.')
print('\t The format is:   list[start:end:step]')
print('\t my_list[0:6:2] = \t', my_list[0:6:2])


print('\n\n Python is open to interpretation')
print('\t We can say:   my_list[-1:2:-1]')
print('\t We are starting at the end, going to the 2nd spot, using a neg step. So in reverse')
print('\t my_list[-1:2:-1] = \t', my_list[-1:2:-1])
print(' Remember that even going in reverse, we need an open colon.')


print('\n\n We can go in reverse, by 2 steps, all the way to the beginning.')
print('\t my_list[::-2] =\t', my_list[::-2])


print('\n\n Now we slice strings. ')
sample_url = 'http://NCharlesTerry.com'
print('\t sample_url = ', sample_url)
print('\t Get the .com with:   sample_url[-4:] = \t', sample_url[-4:])
print(' It starts at the 4th char from the end and goes to the end.')


print('\n Now get just the body. We need to know the count.')
print('\t sample_url[7:-4] = \t', sample_url[7:-4])
print(' Note it does not have to be -4 at the end, it can be the positive representation as well. ')