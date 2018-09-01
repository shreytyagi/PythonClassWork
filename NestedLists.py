y=list
x=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
finalsum=int(0)
tempsum=int(0)
for i in range(0,4):
    tempsum=0
    for j in range(0,3):
        tempsum+=x[i][j]
    if tempsum>finalsum:
        finalsum=tempsum
        y=x[i]
print(y)
print(finalsum)



        
    
