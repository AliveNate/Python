# ===============================================================
# Printing out and formatting dates and times.
print('\n\n')
# Datetime library
# https://docs.python.org/3/library/datetime.html

# we need another library
import datetime

print('auto format (year, month, day, hour, minute, second)')
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
print('---------------')

# Now using specific date format from library above.
print('# Now using specific date format from library above.')
sentence_Date = '{:%B %d %Y}'.format(my_date)
print(sentence_Date)
print('---------------')

# Now we will use libary abbrev. %A and %J for day of the
print('We want the date in format, and specifics about that date. ')
print('Complicated. We are only passing in one reference [my_date] but we have 3 brackets.')
print('In each bracket we need a 0 to reference [my_date] the object passed in.')
print('%B %d %Y %A %j are all inherent library abbreviations. Found on webpage above')
print('EX. %A will reference the library and know that the date was a Saturday.')
print('---------------')
sentence_Date2 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence_Date2)
# ===============================================================
# ===============================================================