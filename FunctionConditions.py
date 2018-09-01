a=input('Enter a string: ')
if a.isalpha()==1:
    print('Only Alphabets')
elif a.isnumeric()==1:
    print('Only Numbers')
else:
    print('Both Alphabets and Numbers')
b=input('Enter the character/string to be replaced: ')
c=input('Enter the character/string to replace: ')
a=a.replace(b,c)
print(a)


