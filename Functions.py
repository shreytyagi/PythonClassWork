def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))

def myfunction(fname):
    print(fname+" box")
myfunction("Email")
myfunction("Phone")
myfunction("Address")

def myfunction2(country="Norway"):
    print("I am from "+country)
    myfunction
