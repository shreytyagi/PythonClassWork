list1=[0,1,0,1,1,1]
i=0
n=6
print(list1)
for i in range(0,6):
    if(list1[i]==0):
        list1[i]=1
    else:
        list1[i]=0
print(list1)
i=0
list2=list1
for i in range(0,5):
    if(i<(n-1)):
        list2[i]=list1[i]+list1[i+1]
    else:
        list2[i]=list1[i]+list1[0]    
print(list2)


