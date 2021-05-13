import datetime

# Date e hora atual
print(datetime.datetime.now())

treehouse_start = datetime.datetime.now()

treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)

treehouse_start = treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)
print(treehouse_start)


a = datetime.datetime.now() - treehouse_start
print(a)
print(a.days)
print(a.microseconds)
print(a.seconds)

hours_worked = round(a.seconds/3600)
print(hours_worked)

## timedelta
now = datetime.datetime.now()
print(datetime.timedelta(hours=5))

# avançando a data
a = now + datetime.timedelta(days=3)
print(a)

antes = now + datetime.timedelta(days=-5)
print(antes)


print(now.date())
print(now.time())

hour = datetime.timedelta(hours=1)

workday = hour * 9

tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)
print(tomorrow)

b = tomorrow + workday
print(b)






