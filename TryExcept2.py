print("Enter two numbers: ")
x=input("Enter 1st No: ")
y=input("Enter 2nd No: ")
try:
    if int(x) > int(y):
        print(x+ ' is greater')
    else:
        print(y+ ' is greater')
except:
    print("you didnt enter number value")
else:
    print("two numbers compared successfully")
finally:
    print(y+' is greater')
