from datetime import date, time, datetime

d1 = date.today()
print(d1)
print(d1.day, d1.month, d1.year)
t1 = time(12,00,30)
print(t1)


t2 = datetime.now()
print(t2)

d1 = d1.replace(2019,10,31)
t1 = t1.replace(10,29,30)
print(d1)
print(t1)