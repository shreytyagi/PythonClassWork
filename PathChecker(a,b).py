s=str(input("Enter string: "))
count=int(0)
for i in range(0,len(s)):
    if (s[i]=='a'):
        count+=1
if(count==1):
    print("Successful")
else:
    print("Unsuccessful")
