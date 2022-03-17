

# access to the current datetime.
import datetime

# datetime.now()
now = datetime.datetime.now()
print('\n',now)


#   SPECIFIC TIMES.
current_year = now.year
current_month = now.month
current_day = now.day

print('\nMonth = ', now.month)
print('Year = ', now.year)
print('Day = ', now.day)

print('\n%s/%s/%s' % (now.month, now.day, now.year))
print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))