a=str(input("Enter an email id: "))
al=len(a)
flag=int(0)
b=str('')
for i in range (0,al):
    if(flag==1):
        b+=a[i]
    if(a[i]=="@"):
        flag=1
print("Sent from ",b)
