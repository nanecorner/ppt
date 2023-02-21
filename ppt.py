import random

name = input("Enter your name: ")

def select_weapon():
    weapon = 0
    while(weapon not in [1,2,3]):
        weapon = int(input("Select your weapon:\n1. Rock\n2. Paper\n3. Scissors\n"))
    return weapon - 1

def battle(weapon,counterUser,counterComputer):
    weapons = ["Rock","Paper","Scissors"]
    weaponComputer = weapons[random.randint(0,2)]
    weaponUser = weapons[weapon]
    print(name+"|"+weaponUser+" - "+weaponComputer+"|Computer")
    if weaponComputer == weaponUser:
        return "empate",counterUser,counterComputer
    elif weaponComputer == "Rock":
        if weaponUser == "Paper":
            counterUser+=1
            return "wins "+name,counterUser,counterComputer
        else:
            counterComputer+=1
            return "wins computer",counterUser,counterComputer
    elif weaponComputer == "Paper":
        if weaponUser == "Scissors":
            counterUser+=1
            return "wins "+name,counterUser,counterComputer
        else:
            counterComputer+=1
            return "wins computer",counterUser,counterComputer
    else:
        if weaponUser == "Rock":
            counterUser+=1
            return "wins "+name,counterUser,counterComputer
        else:
            counterComputer+=1
            return "wins computer",counterUser,counterComputer


counterUser = 0
counterComputer = 0
while(counterUser < 2 and counterComputer < 2):
    message, counterUser,counterComputer = battle(select_weapon(),counterUser,counterComputer)
    print(message+"\n"+name+"|"+str(counterUser)+" - "+str(counterComputer)+"|Computer")
if counterUser == 2:
    print(name+" wins the game")
else:
    print("Computer wins, try again!")
