#vnumber1 = 10
#vnumber2 = 7

#if vnumber1 < vnumber2:
    #print(vnumber1, " >or< ", vnumber2)
    #print(vnumber1, " is < ", vnumber2)

#elif vnumber1 > vnumber2:
    #print(vnumber1, " >or< ", vnumber2)
    #print(vnumber1, " is > ", vnumber2)


#vnumber = 0
#while vnumber < 6:
    #print (vnumber)
    #vnumber = vnumber + 1

#for i in range(0,10,2):
    #print(i)





#vname = input("what is your name?")
#vletter = vname
#print(vletter)

#i=0
#for vletter in vname:
  #  print(vname[i])
 #   i = i+1









# Pseudo code is code put in plain english
print("You obtained a Dog")
print("You obtained some Dog Food.")
print("You obtained a Dog Bowl")
print("You called Dog")


vdec1 = float(input("Press '1' if Dog responds to the call. Press '2' if Dog does not respond"))
if vdec1 == 1:
    print("You crafted Dog Meal")
    print("You told Dog to eat the food. ")
    vdec2 = float(input("Press '1' if Dog eats the food", ". Press '2' if Dog does not eat the food"))
    while vdec2 == 2:
        vdec2 = float(input("Press '1' if Dog eats the food. Press '2' if Dog does not eat the food"))

    if vdec2 == 1:
        vdec3 = float(input("Press '1' if Dog eats the water", ". Press '2' if Dog does not eat the water"))
        while vdec3 == 2:
            vdec3 = float(input("Press '1' if Dog eats the water", ". Press '2' if Dog does not eat the water"))
        if vdec3 == 1:
            print("You have eaned an Achievement")
            print("Fed the Dog!")

while vdec1 == 2:
    vdec1 = float(input("Press '1' if Dog responds to the call. Press '2' if Dog does not respond"))
    if vdec1 == 1:
        print("You crafted Dog Meal")
        print("You told Dog to eat the food. ")
        vdec2 = float(input("Press '1' if Dog eats the food. Press '2' if Dog does not eat the food"))
        while vdec2 == 2:
            vdec2 = float(input("Press '1' if Dog eats the food. Press '2' if Dog does not eat the food"))

        if vdec2 == 1:
            vdec3 = float(input("Press '1' if Dog eats the water. Press '2' if Dog does not eat the water"))
            while vdec3 == 2:
                vdec3 = float(input("Press '1' if Dog eats the water. Press '2' if Dog does not eat the water"))
            if vdec3 == 1:
                print("You have eaned an Achievement")
                print("Fed the Dog!")










