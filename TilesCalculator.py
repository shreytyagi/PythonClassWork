import math

roomLength=float(input("Enter length of room: "))
roomWidth=float(input("Enter width of room: "))
tileLength=float(input("Enter length of title: "))
tileWidth=float(input("Enter width of title: "))
roomArea=roomLength*roomWidth
tileArea=tileLength*tileWidth
'''completeTiles=roomArea/tileArea
print(completeTiles)
completeTiles=int(completeTiles)
print(completeTiles)'''
tileLengthWise=roomLength/tileLength
tileWidthWise=roomWidth/tileWidth
lengthFlag=int(0)
widthFlag=int(0)

if tileLengthWise%1==0:
    print("\nLength Fits")
    tileWidthWise2=(int(tileWidthWise))
    tileWidthWise=(int(tileWidthWise))
    lengthFlag=1
else:
    print("\nLength Does Not Fit")
    tileLengthWise2=(int(tileLengthWise))
    tileLengthWise=(int(tileLengthWise)+1)

if tileWidthWise%1==0:
    print("Width Fits")
    tileLengthWise2=(int(tileWidthWise))
    tileWidthWise=(int(tileWidthWise))
else:
    print("Width Does Not Fit")
    tileWidthWise2=(int(tileWidthWise))
    tileWidthWise=(int(tileWidthWise)+1)

total=int(tileLengthWise*tileWidthWise)
total2=tileLengthWise2*tileWidthWise2
total3=total-total2

tileLengthWise=str(tileLengthWise)
tileWidthWise=str(tileWidthWise)
total=str(total)
total2=str(total2)
total3=str(total3)

print("Length Wise "+tileLengthWise+" Tiles")
print("Width Wise "+tileWidthWise+" Tiles")
print("Total "+total+" Tiles")
print("Complete "+total2+" Tiles")
print("Incomplete "+(total3)+" Tiles")

