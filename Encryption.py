def alpha(word):
    word2=str('')
    l=len(word)
    word2=str('')
    for i in range(0,l):
        temp=ord(word[i])
        if(96<temp<120):
            temp+=3
        elif(64<temp<88):
            temp+=3
        elif(120<=temp<=122):
            temp-=23
        elif(88<=temp<=90):
            temp-=23
        else:
            temp=42
            
        word2+=chr(temp)
    return word2


a=input('Enter a word: ')
print(alpha(a))

'''yebkzela'''
