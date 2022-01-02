
'''This is a Monopoly console based game that I am building'''

import random
import time

#Stores PLayer Spaces
Players = []
#Stores Player ICons
PIcons = []
PSpace = 0.
#stores players money
PlayerMon = []
#store ids of all properties
Property = ["GO", "Medditaranean Avenue", "Baltic Avenue", "Reading Railroad", "Central Avenue","Vermont Avenue","Conneticut Avenue","St.Charles Place","Electric Company","States Avenue",
"Virginia Avenue","Pennsylvania Railroad","St.James Place","Tennessee Avenue","New York Avenue","Kentucky Avenue","Indiana Avenue","Illinois Avenue","B&O Railroad","Atlantic Avenue","Ventor Avenue",
"Water Works","Marvin Gardens","Pacific Avenue","North Carolina Avenue","Pennsylvania Avenue","Short Line","Park Place","Boardwalk"]
#stores price of each property
PropMon = [0,60,60,200,100,100,120,140,150,140,160,200,180,180,200,220,220,220,240,200,260,260,150,280,300,300,320,200,350,400]
#Declares if Property is owned or not
PropOwn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#stores rent of each property
PropRent = [0,2,4,16,6,6,8,10,10,12,16,14,14,16,18,18,20,16,22,22,24,26,26,28,16,35,50]
#Declares who owns the property
WhoOwn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#how many players
print("Hello there, welcome to Monoply. How many players are there?")
PNum = input()
PNum = int(PNum)
print("Okay, so there are {} players.".format(PNum))

#finding icons
for i in range(PNum):
    print("Player {} choose an icon".format(i+1))
    PIcon = input()
    PIcons.append(PIcon)

time.sleep(1)
print("Okay Players, let's get started!")

for c in range (PNum):
    PlayerMon.append(1500)
#Finding each Players Board Space
for f in range(PNum):
    Players.append(PSpace)

time.sleep(2)


#main game
while True:
    for a in range(PNum):
        #defines variables in the code
        OldSpace = Players[a]
        PRoll = random.randint(1,6)
        Players[a] = (Players[a] + PRoll) % 8  
        print("Player {} ({}) rolled a {}".format(a+1,PIcons[a],PRoll))
        time.sleep(1)
        CurrSpace = Players[a]
        CurrProp = Property[int(CurrSpace)]
        CurrPropMon = PropMon[int(CurrSpace)]
        
        if CurrSpace < OldSpace:
            time.sleep(0.1)
            print("Congratulations! You just passed GO! Here is 200$!")
            PlayerMon[a] = PlayerMon[a] + 200
            print("Player {} now has {}".format(a+1, PlayerMon[a]))
        time.sleep(0.5) 
        print("Player {} ({}) landed on Property {} which costs {}. Would you like to buy this property? Yes/No".format(a+1,PIcons[a],CurrProp,CurrPropMon))
        PChoice = input()
        PChoice = PChoice.lower()
        if(PChoice == "yes"):
            #Makes sure that you don't buy a property that you already own
            if WhoOwn[int(CurrSpace)] == a+1:
                print("Oh, this is your property! You can't buy this again!")
            else:
                #Makes you pay rent for properties that belong to others if you land on it
                if PropOwn[int(CurrSpace)] == 1 and WhoOwn[int(CurrSpace)] != a+1:
                    print("I'm sorry, but this property is already owned. You have to pay off the rent.")
                    PlayerMon[a] = PlayerMon[a] - PropRent[int(Players[a])]
                    print("Player {} now has {} dollars".format(a+1, PlayerMon[a]))
                    PlayerMon[WhoOwn[int(Players[a])]] = PlayerMon[WhoOwn[int(Players[a])]] + PropRent[int(Players[a])]
                    print("player {} now has {} dollars".format(WhoOwn[int(Players[a])],PlayerMon[WhoOwn[int(Players[a])]]))
                else:
                    #stops you from buying the property if you don't have enough money
                    if(PChoice == "yes" and PlayerMon[a] < CurrPropMon):
                        print("I'm sorry, but you do not have sufficient funds to buy this property")
                    else:
                        #goes through the buying of the property process
                        time.sleep(0.7)
                        print("Okay, so you are buying {}".format(CurrProp))
                        PlayerMon[a] = PlayerMon[a]-CurrPropMon
                        time.sleep(0.5)
                        print("Player {} now has {} dollars".format(a+1,PlayerMon[a]))
                        PropOwn[int(CurrSpace)] = 1
                        WhoOwn[int(CurrSpace)] = a+1
                        time.sleep(0.5)
                        print("{} is now owned.".format(CurrProp))          
        else:
            #tells player that it was their property anyway
            print("Okay, so you are not buying {}".format(CurrProp))
            if WhoOwn[int(CurrSpace)] == a+1:
                print("Oh, this is your property! It didn't matter anyway!")
                #makes player pay rent even if they say "no"
            if PropOwn[int(CurrSpace)] == 1 and WhoOwn[int(CurrSpace)] != a+1:
                print("I'm sorry, but this property is already owned. You have to pay off the rent. You can't just avoid that by choosing no.")
                PlayerMon[a] = PlayerMon[a] - PropRent[int(Players[a])]
                print("Player {} now has {} dollars".format(a+1, PlayerMon[a]))
        
        print("The Current Space is {}".format(CurrSpace))
        time.sleep(0.1)
        print("The Previous Space was {}".format(OldSpace))
        time.sleep(1) 
        input()
        
        
