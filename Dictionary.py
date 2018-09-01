a = {
    "Name" : "XYZ",
    "Class" : "123",
    "Branch" : "CSE"
    }

print(a)

a["Name"]="LANGDA TYAGI"

print(a)

b=len(a)

print("Length of a = ",b)

a["Year"]="2000"

print(a)

del(a["Name"])

print(a)

b = {
    "Naam" : "XYZ",
    "Kaksha" : "123",
    "Shaakha" : "CSE"
    }

b=a

print(b)

print(a.keys())
print(a.values())
print(a.items())

a.update(b)

print(a)
