#Title Sequence

def title():
    print("""
╦  ┌─┐┌─┐┌┐┌┌─┐┬ ┬  ╔╦╗┬ ┬┌┐┌┌─┐┌─┐   ╔═╗┌┬┐┌─┐┬─┐┬ ┬  ┌─┐┌─┐  ┌─┐┌─┐┬─┐┌┬┐┌─┐┌─┐┌┐┌┌─┐
║  │ ││ ││││├┤ └┬┘   ║ │ ││││├┤ └─┐   ╚═╗ │ │ │├┬┘└┬┘  │ │├┤   │  ├─┤├┬┘ │ │ ││ ││││└─┐
╩═╝└─┘└─┘┘└┘└─┘ ┴    ╩ └─┘┘└┘└─┘└─┘┘  ╚═╝ ┴ └─┘┴└─ ┴   └─┘└    └─┘┴ ┴┴└─ ┴ └─┘└─┘┘└┘└─┘
""")
def end():
    print("""
╔╦╗┬ ┬┌─┐  ╔═╗┌┐┌┌┬┐
 ║ ├─┤├┤   ║╣ │││ ││
 ╩ ┴ ┴└─┘  ╚═╝┘└┘─┴┘
 """)
print("You are playing:")
print(title())

#Character Choosing
character = int(input("""
press 1 to play as Daffy Duck
press 2 to play as Bugs Bunny
press 3 to play as Wile E. Coyote
press 4 to play as Roadrunner
"""))

if character == 1:
    print("You are playing as Daffy Duck")
    character = "Daffy Duck"
if character == 2:
    print("You are playing as Bugs Bunny")
    character = "Bugs Bunny"
if character == 3:
    print("You are playing as Wile E. Coyote")
    character = "Wile E. Coyote"
if character == 4:
    print("You are playing as Roadrunner")
    character = "Roadrunner"


#Choice 1
c1 = int(input("""
Your house starts shaking
#1. Keep watching tom and jerry
#2. Check the window
press '1' for #1, press '2' for #2
"""))

#watching tom and jerry
if c1 == 1:
    print("You continue watching Tom and Jerry")
while c1 != 2:
    c1 = int(input("""Do you
#1. Keep watching tom and jerry
#2. Check the window
press '1' for #1, press '2' for #2
"""))
#Check the window
if c1 == 2:
    print("You see the mushroom cloud of an atomic bomb above Loony town")
    print("You run to your room and collect the most important things in a nuclear apocalypse")
    inventory = []

#INVENTORY

#item1
i1 = int(input("""
You grab your bag and start to throw things in
press '1' to throw the thing in your bag
press '2' to move on to the next thing in your room\n
You grab a knife. do you take it?
    """))
if i1 == 1:
    inventory.append("Knife")
    print("you move on to the next item")
if i1 == 2:
    print("you move on to the next item")
#item 2
i2 = int(input("There is a camera. do you take it?"))
if i2 == 1:
    inventory.append("Camera")
    print("you move on to the next item")
if i2 == 2:
    print("you move on to the next item")
#item 3
i3 = int(input("""you find your trustworthy dog Doggo.
Do you take him with you?
            """))
if i3 == 1:
    inventory.append("Doggo")
    print("'Come on Doggo, Lets go'")
if i3 == 2:
    print("you shot Doggo to end his suffering")
    print("you don't regret your decision because he was a bad dog anyways")
#item 4
i4 = int(input("There is an aid kit. do you take it?"))
if i4 == 1:
    inventory.append("First Aid Kit")
    print("you move on to the next item")
if i4 == 2:
    print("you move on to the next item")
#item 5
i5 = int(input("There is an empty waterbottle. do you take it?"))
if i5 == 1:
    inventory.append("Waterbottle")
    print("you move on to the next item")
if i5 == 2:
    print("you move on to the next item")
#item 6
i6 = int(input("There is a Gun. do you take it?"))
if i6 == 1:
    inventory.append("Gun")
    print("you move on to the next item")
if i6 == 2:
    print("you move on to the next item")
print("you walk outside and check your bag to see: ",inventory)


#choice 2
c2 = int(input("""
#1. bike to city to find survivors
#2. bike to fallout shelter near your house
"""))
#CITY STORY
if c2 == 1:
    print("You bike to the city and find Tweety Bird and Sylvester in the town.")
    print("Suprisingly, Sylvester isn't trying to eat Tweety.")
    print("None of you have food and you all die. ")
    print(end())

#SHELTER STORY
if c2 == 2:
    print("There is already a long line to go into the shelter")
    print("You ask around and find out that the line could take up to 10 hours")
    c3 = int(input("""
#1. wait in line
#2. find another shelter
"""))
    #choice 3
    if c3 == 1:
        print("After waiting just 20 minutes people start to collapse from radiation")
        pause = input("Press enter to continue")
        print("You manage to sneak near the front of the line to avoid anymore radiation")
        print("""
Another hour passes by and you finally get into the shelter only to realize
that it has been run over by rebels trying to loot the shelter. """)
        pause = input("Press enter to continue")
        #choice 4
        c4 = int(input("""
#1. bike away from shelter
#2. fight back with whatever you have
"""))
        if c4 == 1:
            print("You try to bike away but the rebels shot the tire of your bike")
            print("You keep on running and get shot in the leg. ")
            if "First Aid Kit" in inventory:
                print("You patch up your leg with the first aid kit and manage to limp away from the shelter. ")
                pause = input("Press enter to continue")
                print("You make it to the city and find some friends. ")
                print("none of you have water and you all eventually die of thirst.")
                print(end())
            else:
                print("You fall down and the rebels catch up to you")
                print("They mercilessly shoot you down while you bleed to death. ")
                print(end())
        if c4 == 2:
            if "Knife" in inventory:
                print("You take out your knife to fight back")
                print("You stab the nearest enemy and leave him to bleed. ")
                pause = input("Press enter to continue")
                print("There are too many of them and you get overpowered")
                c5 = int(input("""They offer for you to join them in their crusade to change the world as it is
#1. Accept
#2. Decline"""))
                if c5 == 1:
                    print("They provide food and water in exchange for help in their crusade")
                    pause = input("Press enter to continue")
                    print("You reluctantly help them but at least you are safer now that you are in a group.")
                    print("You realize that this is what your life is now, and there is no changing it")
                    print(end())
                if c5 == 2:
                    print("They drag you across the rough terrain and set up a guillotine")
                    print("You realize that this is the end of the road for you.")
                    print(end())
            if "Gun" in inventory:
                print("you take out your gun to fight back")
                pause = input("Press enter to continue")
                print("You pull the trigger and realize there are no bullets in the chamber or the magazine")
                print("The people in the shelter mutilate you and leave you to bleed to death")
                print(end())
            if "Gun" and "Knife" not in inventory:
                print("You have nothing to fight back with.")
                print("The people in the shelter laugh at you while they shoot you down with their guns. ")
            elif "Knife" and "Gun" in inventory:
                print("you take out your knife and your gun to fight them.")
                print("You pull the trigger and realize there are no bullets in the chamber or the magazine")
                pause = input("Press enter to continue")
                print("You are glad you brought the knife and you stab the enemy nearest to you.")
                print("There are too many of them and you get overpowered")
                c5 = int("""They offer for you to join them in their crusade to change the world as it is
#1. Accept
#2. Decline
""")
                if c5 == 1:
                    print("They provide food and water in exchange for help in their crusade")
                    print("You reluctantly help them but at least you are safer now that you are in a group.")
                    print("You realize that this is what your life is now, and there is no changing it")
                    print(end())
                if c5 == 2:
                    print("They drag you across the rough terrain and set up a guillotine")
                    print("You realize that this is the end of the road for you.")
                    print(end())
    #choice 3
    if c3 == 2:
        print("You bike 20 miles to the next city over and find that there is no other shelter in a 50 mile radius.")
        print("You realize you didn't bring any food or water with you")
        print("You try to bike back to the shelter to stock up on food and water")
        print("You pass out halfway to the shelter")
        print(end())

