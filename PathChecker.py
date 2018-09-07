AB=int(input("Enter value of AB: "))
BC=int(input("Enter value of BC: "))
CD=int(input("Enter value of CD: "))
DA=int(input("Enter value of DA: "))
AC=int(input("Enter value of AC: "))
BD=int(input("Enter value of BD: "))

mi=str("DA")
midn=int(DA)
if (AB+BD)<midn:
    mi="AB+BD"
    midn=int(AB+BD)
if (AC+CD)<midn:
    mi="AC+CD"
    midn=int(AC+CD)
if (AB+BC+CD)<midn:
    mi="AB+BC+BD"
    midn=int(AB+BC+CD)
if (AC+BC+BD)<midn:
    mi="AC+BC+BD"
    midn=int(AC+BC+BD)

print(mi)
print(midn)


