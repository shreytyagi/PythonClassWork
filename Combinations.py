import itertools
str1=list(input())
print(str1)

x=input("Enter character to search: ")
count=int(0)
count2=int(0)

n=int(input("Enter combination number: "))
k=itertools.combinations(str1,n)
for i in list(k):
    count2+=1
    for j in range(0,n):
        if i[j]==x:
            print(i)
            count+=1

print("Probability = ",str(count/count2))

