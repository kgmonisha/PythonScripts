import datetime

dt1 = datetime.datetime(2019, 1, 8, 10)
dt2 = datetime.datetime(2019, 1, 10, 20)
print(dt2 > dt1)
delta = dt2 - dt1

print(delta.days)
print(delta.seconds)

now = datetime.datetime.now()
deltayear = datetime.timedelta(days=365)
deltayear = datetime.timedelta(weeks=1)
print(now+deltayear)
