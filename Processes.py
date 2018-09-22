n=int(input("Enter number of processes: "))
b=[]
for i in range(0,n):
    print("Enter burst time for P",str(i+1),": ",end="")
    b.append(int(input()))

s=int(input("Enter start time: "))

w=[]
temp=int(0)

for i in range(0,n):
    w.append(temp)
    temp=temp+b[i]

t=[]
temp=0

for i in range(0,n):
    temp=temp+b[i]
    t.append(temp)

print("Process\tBurst\tWaiting\tTurnAround")
for i in range(0,n):
    print("P",i+1,"\t",b[i],"\t",w[i],"\t",t[i])
