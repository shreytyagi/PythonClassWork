list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
i=0
n=5
print(list1)
while(i<n):
    if(i<(n-1)):
        list2[i]=list1[i]+list1[i+1]
    else:
        list2[i]=list1[i]+list1[0]    
    i+=1
print(list2)
