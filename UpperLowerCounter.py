x=str(input("Enter a string: "))
xs=len(x)
y=str('')
lower=upper=int(0)
for i in range (0,xs):
    if 97<=ord(x[i])<=122:
        lower+=1
    if 65<=ord(x[i])<=90:
        upper+=1
print("Lower = ",str(lower),"\nUpper = ",str(upper))
