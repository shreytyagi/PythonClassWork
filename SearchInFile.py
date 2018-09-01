f=open("file.txt","r")

count=int(0)
o=int(0)

while (o!=1 and o!=2):
    o=int(input("1. Character Search\n2. String Search\nChoose Option: "))

if o==1:
    c=str(input("Enter the character to search: "))
    for x in f:
        xl=x.split()
        for i in xl:
            for j in i:
                if j==c:
                    count+=1

if o==2:
    w=str(input("Enter the word to search: "))
    for x in f:
        xl=x.split()
        for i in xl:
            if i==w:
                count+=1

if count==0:
    print("Not Found.")
else:
    print("Found ",str(count)," times.")
