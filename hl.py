import mainmenu
import random
import transport_system



def higher_lower():
    print("***Higher or Lower***")
    print(" **Play?**")
    print(" **Y/N**") #same as the one further down
    p = input() #but done exclusivley for the beginging
    transport_system.wrong_platform_check(p, mainmenu.menu) #because its done barely differently
    num = random.randint(1, 100)
    attempt = 1
    goto = 50
    go = 45
    print("***A number between 1 and 100 has been selected, can you guess what it is?")
    guess = int(input("Whats your guess?"))

    while guess != num:
        print("Wrong! Guess again!")
        hl(guess, num)
        attempt = attempt + 1
        guess = int(input("Whats your new guess?"))
    print("You got it! It took you", attempt, "attempts!")

    print("What do you wanna do?")
    print("(1) Play again")
    print("(2) Go back to main menu")
    ticketmachine = int(input())
    transport_system.train(ticketmachine, higher_lower, mainmenu.menu)
def hl(g, r):
    if g > r:
        print("Your number was higher than the answer, you need to go lower")
    elif g < r:
        print("Your number was lower than the answer, you need to go higher")