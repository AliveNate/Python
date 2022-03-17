

print('\n Collect a string and test the length.')


x = 5
y = 10
z = 22

if x > y:
    print('\tX is greater than Y')
elif x < z:
    print('\tx is greater than z')
elif 5 > 2:
    print('\t5 is greater than 2')
else:
    print('\tif and elif(s) never ran.')


print('\n Remember, two statements are right, but we are using elif. Only get one statement.')
print('\n\n')

user_in = input(" Please enter a string: ")
if len(user_in) < 6:
    print('\t Your string is too short.')
    print('\t Enter more than 6 characters next time.')



num_input = input('\n Please enter an integer?')
print('\t Note. The 4 lines below wont work. We havent converted to an integer yet.')
#   if num_input % 2 == 0:
#       print('\t Your number is even.')
#   else:
#      print('\t Your number is odd.')
num_input = int(num_input)
print('\t Just converted.')
if num_input % 2 == 0:
    print('\t\t Your number is even.')
else:
    print('\t\t Your number is odd.')



print('\n\n Determine what type of triangle we have.')
print('\t Scalene = All sides hav edifferent lengths.')
print('\t Isosceles = Two sides have the same length.')
print('\t Equilateral = all sides are equal. ')

a = int(input('\t\tThe length of side a?  '))
b = int(input('\t\tThe length of side b?  '))
c = int(input('\t\tThe length of side c?  '))

if a != b and b != c and a != c:
    print('\t This is a scalene triangle.')
elif a == b and b == c:
    print('\t This is an equilateral triangle.')
else:
    print('\t This is an isosceles triangle.')


