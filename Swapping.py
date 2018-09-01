def show(x,y):
    print("First Value: ",x)
    print("Second Value: ",y)
    
def swap(x,y):
    return(y,x)

a=int(input("Enter a: "))
b=int(input("Enter b: "))

show(a,b)

a,b=swap(a,b)

show(a,b)
