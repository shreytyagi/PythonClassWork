AB=int(input("Enter value of AB: "))
BC=int(input("Enter value of BC: "))
CD=int(input("Enter value of CD: "))
DA=int(input("Enter value of DA: "))
AC=int(input("Enter value of AC: "))
BD=int(input("Enter value of BD: "))

mi=str("DA")
midn=DA
if (AB+BD)<midn:
    mi="AB+BD"
    midn=AB+BD
if (AC+CD)<midn:
    mi="AC+BD"
    midn=AC+BD
if (AB+BC+CD)<midn:
    mi="AB+BC+BD"
    midn=AB+BC+CD
if (AC+BC+BD)<midn:
    mi="AC+BC+BD"
    midn=AC+BC+BD

print(mi)
print(midn)


