from random import randint
vint = (randint(0,100))
print(vint + 10)
vguess = int(input("guess a number from 0-100"))
vcounter = 0

while vguess > vint:
    print("The number is lower")
    vguess = int(input("guess a number from 0-100"))
    vcounter = vcounter + 1
    while vguess < vint:
        print("The number is higher")
        vguess = int(input("guess a number from 0-100"))
        vcounter = vcounter + 1
while vguess < vint:
    print("The number is higher")
    vguess = int(input("guess a number from 0-100"))
    vcounter = vcounter + 1
    while vguess > vint:
        print("The number is lower")
        vguess = int(input("guess a number from 0-100"))
        vcounter = vcounter + 1
if vguess == vint:

    print("Congratulations, that number is correct")
    print("You took", vcounter, "guesses")
