##if else

vscore = 75

if vscore >= 50:
    print("\nPass")
else:
    print("\nFail")



##if in
vmonth = "september"
vletter = "e"

if vletter in vmonth:
    print("There is a letter", vletter, "in", vmonth)
else:
    print("There is not a letter", vletter,"in",vmonth)

print (len(vmonth))

vchoice = input("entar nombar 1 to 3: ")

if vchoice == "1":
    print("y u choosen 1")
elif vchoice == "2":
    print("y u choosen 2")
elif vchoice == "3":
    print("y u choosen 3")
else:
    print("plez choosen 1, 2, oar 3.")

input("\n\nplez poosh a bottun on kaybord, den poosh entar")





vword = input("enter a word:")

vword = vword.lower()

score = 0

for letter in vword:
    if letter == "a":
        score = score + 5
        print(letter, "is worth 5")
    elif letter == "e":
        score = score + 4
        print(letter, "is worth 4")
    elif letter == "i":
        score = score + 3
        print(letter, "is worth 3")
    elif letter == "o":
        score = score + 2
        print(letter, "is worth 2")
    elif letter == "u":
        score = score + 1
        print(letter, "is worth 1")
    else:
        score = score + 0
        print(letter, "is worth 0")

print("total score is",score)
