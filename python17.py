#MODULES
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.ceil(45.89))
print(math.floor(45.89))
print(math.pi)
print(math.pow(2,3))


import random as r
#random number
print(r.randint(1,10))
print(r.randrange(1,10,2))
print(r.random()) #0.0 to 1.0
print(r.uniform()) #floating numbers
f=["apple","pineaple","grapes"]
print(r.choice(f))
print(r.choices(f,k=2))


#random 4 digit otp
otp=r.randint(0000,9999)
print(otp)

import datetime as d
print(d.datetime.now())
print(d.date.today())
#only time
d1=d.datetime.now()
print(d1.time())
# day month year 
print(d1.day())
print(d1.month())
print(d1.year())

#own add
print(d.date(2026,2,12))
#date format  -->yy/mm/dd -->dd/mm/yyyy
x=d.datetime.now()
print(x.strftime("%d/%m/%y"))
print(x.strftime("%S:%M:%H"))

#difference
currentdate=d.date(2026,5,19)
birthdate=d.date(2005,10,31)
print(currentdate-birthdate)

#future date
currentdate=d.datetime.now()
future=currentdate+d.timedelta(days=60)
print(future)