print('\n\nQ1) X Triangle\n')
a='x'
n=int(input('Enter no. of rows: '))
b=a
for i in range(0,n):
    print(b)
    b+=a

    
print('\n\nQ1) Binary Triangle\n')
a="1"
b="0"
n=int(input('Enter no. of rows: '))
c=b
temp=''
for i in range(0,n):
    for j in range(0,i+1):
        if c==b:
            c=a
            temp+=a
        else:
            c=b
            temp+=b
        j+=1
    print(temp)
    temp=''
    i+=1

    
print('\n\nQ3) Number Triangle\n')
n=int(input('Enter no. of rows: '))
temp=''
count=1
for i in range(0,n):
    for j in range(0,i+1):
        if count==10:
            count=0
        a=str(count)
        temp+=a
        count+=1
    print(temp)
    temp=''


print('\n\nQ4) HexaDecimal Triangle\n')
n=int(input('Enter a number (at least 12 digit long): '))
n=hex(n)
n=str(n)
m=len(n)
temp=''
count=int(0)
'''print('HexaDecimal = ',n)
print('Length = ',m)'''
for i in range(0,m):
    for j in range(0,i+1):
        temp+=n[count]
        count+=1
        if count==m:
            break
    print(temp)
    temp=''
    if count==m:
        break




