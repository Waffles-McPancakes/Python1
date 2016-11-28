month = "october"

print(month.upper())
print(month.lower())

x = float(34)
y = float(24.9)
print(x,y,x-y)

vmonth = "september"
vletter = vmonth[0]
print(vletter)

i = 0
for letter in vmonth:
    print(vmonth[i])
    i = i+1

vmonth = "october"
print(vmonth[:4])


vmessage = "This sentence is false"
print(vmessage)
print(vmessage.find('false'))

print(vmessage.find('no'))

vstring1 = input("What is your first name?")
vstring2 = input("last name?")
print("Your name is " + vstring1 + " " + vstring2)

vinteger = 10
print(vinteger)
vfloat = float(vinteger)
print(vfloat)

x = 14
y = 12
print(x*y)

z = 365
a = 24
print(z*a*x)
d = 60
print(z*a*x*d)

vnumber1 = 5
vnumber2 = 1

if vnumber1 > vnumber2:
    print(vnumber1, "is bigger")
vnumber = 0
while vnumber < 10:
    print(vnumber)
    vnumber=vnumber + 1

for i in range(0,20,2) :
    print(i)
