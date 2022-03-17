import sys
import os

'''Decorators: first class functions allow us to treat other functions like an object
Here the outer function does not take parameters.
The Inner function does not create the message, but does have access to it.
Note: I could not get that Hi simply on that my return was a tab in too far.
'''



def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')


print('\n--------------------------')
'''This is complicated. The decorated_display is actually a function since we added
the () at the end. So it executes the wrapper_function which executes the display
function that prints out. '''
# --> can't decorate. Means display_info will get a third param
# if we add *args, **kwargs to the decorator function
# they allow us to accept any arbitrary params for functions
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info("John", 25)

display()

