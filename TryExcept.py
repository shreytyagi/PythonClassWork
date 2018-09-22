a=[]
for i in range(0,8):
    try:
        print("Enter a number: ",end="")
        a.append(int(input()))
    except:
        a.append("Error")

try:
    print(a[0]+a[1])
except:
    print("Error")

try:
    print(a[2]*a[3])
except:
    print("Error")

try:
    print(a[4]/a[5])
except:
    print("Error")

try:
    print(a[6]-a[7])
except:
    print("Error")
