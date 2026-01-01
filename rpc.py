import random
import mainmenu
import transport_system

def rockpaperscisors():
    print("***Rock Paper Scissors***")
    print(" **Play?**")
    print(" **Y/N**") #same as the one further down
    p = input() #but done exclusivley for the beginging
    transport_system.wrong_platform_check(p, mainmenu.menu) #because its done barely differently
    print("   (1) Rock")
    print("   (2) Paper")
    print("   (3) Scissors")
    mychoice = int(input("What do you want?"))
    translate("You", mychoice)
    opchoice = random.randint(1,3)
    translate("They", opchoice)
    decider(mychoice, opchoice)
    print("What do you wanna do?")
    print("(1) Play again")
    print("(2) Go back to main menu")
    ticketmachine = int(input()) #Asks the user where they wanna go
    transport_system.train(ticketmachine, rockpaperscisors, mainmenu.menu) #See comment in transport_system.py

def translate(youthey, choice):
    print(youthey)
    if choice == 1:
        print("Chose Rock")
    elif choice == 2:
        print("Chose Paper")
    elif choice == 3:
        print("Chose Scissors")
    else:
        print("Listen prick")

def decider(one, two):
    if one == 1 and two == 2: #Rock Paper
        print("You Lose!")
    elif one == 2 and two == 1: #Paper Rock
        print("You Win!")
    elif one == 3 and two == 1: #Scissors Rock
        print("You Lose!")
    elif one == 1 and two == 3: #Rock Scissors
        print("You Win!")
    elif one == 2 and two == 3: #Paper Scissors
        print("You Lose!")
    elif one == 3 and two == 2: #Scissors Paper
        print("You Win!")
    elif one == two:
        print("Draw!")
    else:
        print("How?")
def fuck(x1, x2, x3):
    x3 = x1 + x2
    print(x3)