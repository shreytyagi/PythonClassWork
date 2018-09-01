import math
a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))
d=float((b*b)-(4*a*c))
if(d<0):
    print('Invalid Values')
else:
    d=math.sqrt(d)
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print('Roots: ',x1,' and ',x2)

