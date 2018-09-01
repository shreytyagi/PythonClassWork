x=str(input("Enter a string: "))
xs=len(x)
y=str('')
z=int(input("Enter index to delete: "))
for i in range (0,xs):
    if i!=z:
        y+=x[i]
print(y)
