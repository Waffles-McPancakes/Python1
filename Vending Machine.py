
twix = 10.20
mars = 11.60
cadbury = 13.10

print("""
Twix = 10.20 HKD
Mars = 11.60 HKD
Cadbury = 13.10 HKD
""")

bar = int(input("press 1 for Twix,press 2 for Mars,press 3 for Cadbury"))
moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))


if bar == 1:


    if moneys > twix:
        print("You input",moneys,"Bar cost",twix,"Change =",moneys-twix)
    elif moneys<twix:
        print("input more money please")
        moneys = int(input("Add money for the chacolate bar. only input $5.00, $10.00, $20.00"))


elif bar == 2:
    moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))
    if moneys != 5 and moneys !=10 and moneys !=20:
        print("only input 5,10,20")
    if moneys > mars:
        print("You input",moneys,"Bar cost",mars,"Change =",moneys-mars)
    elif moneys<mars:
        print("input more money please")


elif bar == 3:
    moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))
    if moneys != 5 and moneys !=10 and moneys !=20:
        print("only input 5,10,20")
    if moneys > cadbury:
        print("You input",moneys,"Bar cost",cadbury,"Change =",moneys-cadbury)
    elif moneys<cadbury:
        print("input more money please")

else:

    while bar != 1 and bar!= 2 and bar != 3 :
        print("please input a real chocolate bar")
        bar = int(input("press 1 for Twix,press 2 for Mars,press 3 for Cadbury"))
        if bar == 1:
            moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))
            if moneys != 5 and moneys !=10 and moneys !=20:
                print("only input 5,10,20")
            if moneys > twix:
                print("You input",moneys,"Bar cost",twix,"Change =",moneys-twix)
            elif moneys<twix:
                print("input more money please")


        elif bar == 2:
            moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))
            if moneys != 5 and moneys !=10 and moneys !=20:
                print("only input 5,10,20")
            if moneys > mars:
                print("You input",moneys,"Bar cost",mars,"Change =",moneys-mars)
            elif moneys<mars:
                print("input more money please")


        elif bar == 3:
            moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))
            if moneys != 5 and moneys !=10 and moneys !=20:
                print("only input 5,10,20")
            if moneys > cadbury:
                print("You input",moneys,"Bar cost",cadbury,"Change =",moneys-cadbury)
            elif moneys<cadbury:
                print("input more money please")





def machine_change():


    moneys = int(input("Put the money for the chacolate bar. only input $5.00, $10.00, $20.00"))
    if moneys > cadbury:
        print("You input",moneys,"Bar cost",cadbury,"Change =",moneys-cadbury)
    elif moneys<cadbury:
        print("input more money please")
def change():
    if moneys > twix or moneys > mars or moneys > cadbury:
        print("You put",moneys+". Bar cost",cadbury or mars or twix+". Change = ",moneys-cadbury or mars or twix)
