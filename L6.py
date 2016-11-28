"""
x = input("number 1")
y = input("number 2")

def re_cap(x,y):
    if x>y:
        print(y,"is smaller")
    elif x<y:
        print(x,"is smaller")
    elif x==y:
        print(x,"and",y,"are equal")


re_cap(x,y)

def re_cap2():
    print("Ms Mok Smells" * 3)

re_cap2()


z = int(input("choose a number"))

def re_cap3(z):
    print((z * 2) + 1)


re_cap3(z)


def f_ask_yes_no(question):
    print("Ask a yes or no question")
    response = None
    while response not in ("yes","no"):
        response = input(question.lower())
    return response

Question = "Would you like a Mars Bar?"
Answer = f_ask_yes_no(Question)

if Answer == "yes":
    print("take mears bar")
if Answer == "no":
    print("no mears bar")

"""

#Menu bar
def menu_bar():
    print("""
    THE ONLY MENU BAR
1. Play Game
2. Settings
3. Friends
4. Exit Game
    """)
    choose = int(input("press the corresponding number to select an option"))
    if choose == 1:
        print("you have started the game")
    elif choose == 2:
        print("There are no settings")
    elif choose == 3:
        print("you have no friends")
    elif choose == 4:
        print("Exiting the game...")

menu_bar()
