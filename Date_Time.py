
'''Directive	Meaning
%a	Weekday name.
%A	Full weekday name.
%b	Abbreviated month name.
%B	Full month name.
%c	Appropriate date and time representation.
%d	Day of the month as a decimal number [01,31].
%H	Hour (24-hour clock) as a decimal number [00,23].
%I	Hour (12-hour clock) as a decimal number [01,12].
%j	Day of the year as a decimal number [001,366].
%m	Month as a decimal number [01,12].
%M	Minute as a decimal number [00,59].
%p	Equivalent of either AM or PM.
%S	Second as a decimal number [00,61].
%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w	Weekday as a decimal number [0(Sunday),6].
%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x	Appropriate date representation.
%X	Apropriate time representation.
%y	Year without century as a decimal number [00,99].
%Y	Year with century as a decimal number.
%Z	Time zone name (no characters if no time zone exists).
%%	A literal ‘%’ character.


now = datetime.datetime.now()
now.hour
now.mintue
now.year
now.day
now.month

'''

import time

print(time.strftime("1_____%H:%M:%S"))

## 12 hour format ##
print(time.strftime("2_____%I:%M:%S"))


# To print current date use:
## dd/mm/yyyy format
print(time.strftime("3_____%d/%m/%Y"))

now = time.strftime("4_____%c")
## date and time representation
print("5_____Current date & time " + time.strftime("%c"))

## Only date representation
print("6_____Current date " + time.strftime("%x"))

## Only time representation
print("7_____Current time " + time.strftime("%X"))

## Display current date and time from now variable (print("Current time %s" % now)


print('\n\n\n============================================')
import datetime

i = datetime.datetime.now()

print("a_____Current date & time = %s" % i)

print("b_____Date and time in ISO format = %s" % i.isoformat())

print("c_____Current year = %s" % i.year)

print("d_____Current month = %s" % i.month)

print("e_____Current date (day) =  %s" % i.day)

print("f_____dd/mm/yyyy format =  %s/%s/%s" % (i.day, i.month, i.year))

print("g_____Current hour = %s" % i.hour)

print("h_____Current minute = %s" % i.minute)

print("i_____Current second =  %s" % i.second)

print("j_____hh:mm:ss format = %s:%s:%s" % (i.hour, i.month, i.second))

