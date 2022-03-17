

"""---------------------------------------------------------------------------
boolean

remember you can set a boolean just based on a result
bool_one =  2**3 == 16
We know that the result of 2**3 = 8 so the bool_one will be set to false.

    Boolean Operators
————————————
True and True is True		1*1=1
True and False is False		1*0=0
False and True is False		0*1=0
False and False is False	0*0=0

True or True is True		1+1=1
True or False is True		1+0=1
False or True is True		0+1=1
False or False is False		0+0=0

Not True is False
Not False is True
# XXX:
"""


bool_one = 2**3 == 16
print('\n The equation 2**3 == 16 doesn\'t work so it is:   ', bool_one)


print('\n\nThe:   and   will inherently return a false, if either part of the expression is false.   1*0 = 0')
print('--------------------\nSet bool_one equal to the result of False and False')
print('\tbool_one = 2<1 and 5>5')
bool_one = 2 < 1 and 5 > 5
print('bool_one = ', bool_one)
print('\n--------------------\nSet bool_two equal to the result of False and True')
print('\tbool_two = -(-(-(-2))) == -2 and 4 >= 16**0.')
bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5
print('bool_two = ', bool_two)
print('\n--------------------\nSet bool_three equal to the result of True and False')
print('\tbool_three = 19 % 4 != 300 / 10 / 10 and False')
bool_three = 19 % 4 != 300 / 10 / 10 and False
print('bool_three = ', bool_three)
print('\n--------------------\nSet bool_four equal to the result of True and True')
print('\tbool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2')
bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
print('bool_four = ', bool_four)
print('\n--------------------\nSet bool_five equal to the result of True and True')
print('\tbool_five = 2>1 and 7<8')
bool_five = 2>1 and 7<8
print('bool_five = ', bool_five)



print('\n\n\n or   or   or')
print('The boolean operator or returns True when at least one expression on either side of or is true. For example:')
print('\t1 < 2 or 2 > 3 is True')
print('\t1 > 2 or 2 > 3 is False.')

'''Or
The boolean operator or returns True when at least one expression on either side of or is true. For example:

1 < 2 or 2 > 3 is True;
1 > 2 or 2 > 3 is False. '''


print('Set bool_one to   True or False')
print('bool_one = 2**3 == 108 % 100 or \'Cleese\' == \'King Arthur\'')
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
print('\tbool_one = ', bool_one)

print('\n bool_two = True or False  =  ')
bool_two = True or False
print('\t bool_two = ', bool_two)

print('\n bool_three = bool_three = 100**0.5 >= 50 or False')
bool_three = 100**0.5 >= 50 or False
print('\t bool_three = ', bool_three)

print('\n bool_four = True or True')
bool_four = True or True
print('\t bool_four = ', bool_four)

print('\n bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1')
bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
print('\t bool_five = ', bool_five)




print('\n\n\n NOT   NOT   NOT')

print('The boolean operator not returns True for false statements and False for true statements.')
print('For example:')
print('not False will evaluate to True, while not 41 > 40 will return False.')
print('-----------------------------')
print('set: bool_one = not True')
bool_one = not True
print('\t\tbool_one = ',bool_one)

print('set: bool_two = not 3**4 < 4**3')
bool_two = not 3**4 < 4**3
print('\t\tbool_two = ', bool_two)

print('set: bool_three = not 10 % 3 <= 10 % 2')
bool_three = not 10 % 3 <= 10 % 2
print('\t\tbool_three = ', bool_three)

print('set: bool_four = not 3**2 + 4**2 != 5**2')
bool_four = not 3**2 + 4**2 != 5**2
print('\t\tbool_four = ', bool_four)

print('set: bool_five = not not False')
bool_five = not not False
print('\t\tbool_five = ', bool_five)

print('\n\n\n This and That (or This, But Not That!)')
print('Boolean operators aren\'t just evaluated from left to right. Just like with arithmetic operators, there\'s an order of operations for boolean operators:')
print('\tnot is evaluated first.')
print('\tand is evaluated next.')
print('\tor is evaluated last.')
print('For example, True or not False and False returns True. If this isn\'t clear, look at the Hint.')
print('Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit. ')

print('\n\tbool_one = False or not True and True')
bool_one = False or not True and True
print('bool_one = ', bool_one)

print('\n\tbool_two = False and not True or True')
bool_two = False and not True or True
print('bool"_two = ',  bool_two)

print('\n\tbool_three = True and not (False or False)')
bool_three = True and not (False or False)
print('bool_three = ', bool_three)

print('\n\tbool_four = not not True or False and not True')
bool_four = not not True or False and not True
print('bool_four = ', bool_four)

print('\n\tbool_five = False or not (True and True)')
bool_five = False or not (True and True)
print('bool_five = ', bool_five)
