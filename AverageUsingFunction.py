def average(*num):
    a=int(0)
    b=len(num)
    for i in num:
        a+=num[i-1]
    print('Total Elements: ',str(b))
    return(a/b)
x=average(1,2,3,4,5,6,7,8,9)
print('Average: ',str(x))
