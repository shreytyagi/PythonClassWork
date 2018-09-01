s=str(input("Enter a string: "))
sl=len(s)
for i in range(0,sl):
    print(s[i])
    bs=str(bin(ord(s[i])))
    bl=len(bs)
    for j in range(0,sl):
        bstemp=""
        for k in range(2,bl):
            bstemp+=bs[k]
    print(bstemp)
    
