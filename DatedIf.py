import datetime

d1=int(input("Enter Date of Date-1: "))
m1=int(input("Enter Month of Date-1: "))
y1=int(input("Enter Year of Date-1: "))
d2=int(input("Enter Date of Date-2: "))
m2=int(input("Enter Month of Date-2: "))
y2=int(input("Enter Year of Date-2: "))

date1=datetime.date(y1, m1, d1)
date2=datetime.date(y2, m2, d2)

date3=date2-date1
days=date3.days
if days<0:
    days=0-days
days=str(days)

print("Number of days: ",days)

