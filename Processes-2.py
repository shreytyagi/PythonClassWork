n=int(input("Enter number of processes: "))
b=[]
w=[]
f=[]
for i in range(0,n):
    print("Enter burst time for P",str(i+1),": ",end="")
    b.append(int(input()))
    f.append(0)

s=int(input("Enter start time: "))
t=int(input("Enter execution time: "))

print(b)

z=int(0)
sum=int(200)
count=int(0)
count2=int(0)
flag=int(0)

while(flag==0):
    for i in range(0,n):
        count+=t
        if f[i]!=1:
            if b[i]>t:
                b[i]=b[i]-t
                print("P -",str(i+1),end=":  ")
                print(str(b[i]))
            else:
                b[i]=0
                count2+=1
                f[i]=count2
                print("P -",str(i+1)," gone")
                print(f)
        sum=sum-n
print(w)
