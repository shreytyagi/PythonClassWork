x=str(input("Enter words (seperated by spaces): "))
xl=x.split()
print(xl)
xs=len(xl)
ms=int(0)
mi=int(0)
for i in range (0,xs):
    if (len(xl[i]))>ms:
        ms=len(xl[i])
        mi=i
print(xl[mi])
    
    
