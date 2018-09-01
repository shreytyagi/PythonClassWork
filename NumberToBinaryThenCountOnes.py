a=int(input("Enter a number: "))
a=bin(a)
print(a)
b=str(a)
c=len(b)
count=int(0)
for i in range (0,c):
      if b[i]=="1":
          count+=1
count=str(count)
print("You'll get ",count," candies")
