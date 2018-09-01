s=str(input("Enter a string: "))
slist=s.split()
sl=len(slist)
slist2=[]
for i in range(0,sl):
    slist2.append(1)
for i in range(0,sl):
    for j in range(0,sl):
        if(i!=j):
            if(slist[i]==slist[j]):
                slist2[j]+=1
sl=(len(slist))
m=(max(slist2))
for i in range (0,sl):
    if slist2[i]==m:
        print(slist[i])
        break;
di={}
print(slist)
print(slist2)

