







vword = input("player 1 enter any word")

vguess = ""
vscore = 0
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
vlength = len(vword)
print("THE WORD HAS",vlength,"LETTERS")

while vguess != vword:

    vguess = input("player 2 guess a letter")

    if vguess in vword:
        print("THAT LETTER IS IN THE WORD")
        print ("That Letter is in position:", (vword.find(vguess) + 1))
        print("There is",vword.count(vguess)," of that letter")
        vscore = vscore + 1
    elif :
        print("")

    else:
        print("THAT LETTER IS NOT IN THE WORD")
        vscore = vscore + 1

if vguess == vword:
    print("YOU HAVE WON THE GAME")
    print("YOU TOOK",vscore,"GUESSES")




