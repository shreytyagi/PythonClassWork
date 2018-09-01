t1=int(0)
t2=int(1)
n=int(input("Enter the number of terms: "))
series=[]

for i in range (0,n):
    series.append(t1)
    nextTerm=t1+t2
    t1=t2
    t2=nextTerm

series.reverse()
print(series)
