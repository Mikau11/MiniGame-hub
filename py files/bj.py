import random
import transport_system

def blackjack():
    print("***Black Jack***")
    transport_system.wrong_platform_check()

    card1 = random.randint(1, 11) #Base
    card2 = random.randint(1, 10) #Cards
    cardf = card1 + card2 #Total of those cards
    twistcard = 0 #Amount thats added on if twist is selected, not important now
    print("Your current total is:", card1 + card2)
    print("What you gonna do?")
    print("(1)Twist")
    print("(2)Stick")
    card = int(input()) #Asks the user what they wanna do
    while card == 1: #twist selected
        twistcard = random.randint(1, 10) #card from earlier is assigned a value
        cardf = cardf + twistcard #Added to total, important to do this inside the loop
        print("You got a:", twistcard) #as if its done outside the loop, eg afterwards
        print("Current Total is:", cardf) #then the value will be whatever it was at the last twist not everything combined
        print("What you gonna do?")
        print("(1)Twist")
        print("(2)Stick")
        card = int(input()) #Asks them again, because its a loop, if they choose twist it stays 1 and goes back up, if stick then it changes to 2, and the file carries on
    if cardf == 21: #Win or lose
        print("You win!")
    elif cardf > 21:
        print("You lost!")
    elif cardf < 21:
        print("You win(kinda)!")

    transport_system.train(blackjack) #See comment in transport_system.py