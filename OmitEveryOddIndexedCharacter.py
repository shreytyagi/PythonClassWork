x=str(input("Enter a string: "))
xs=len(x)
y=str('')
for i in range (0,xs):
    if i%2==0:
        y+=x[i]
print(y)
