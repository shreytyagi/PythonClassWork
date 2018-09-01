word=input()
value=input("Enter value to be searched: ")
d=dict()
for c in word.split():
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
    print(d)
    if (value in d):
        print (value+":"+str(d[value]))
    else:
        print('Not Found')
