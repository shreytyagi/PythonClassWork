import random

word=str('')

for i in range(0,10):
    a=random.randint(65,91)
    word+=chr(a)
print(word)
