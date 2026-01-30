import mainmenu
import random
import transport_system



def higher_lower():
    print("***Higher or Lower***")
    transport_system.wrong_platform_check()
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
    transport_system.train(higher_lower)
def hl(g, r):
    if g > r:
        print("Your number was higher than the answer, you need to go lower")
    elif g < r:
        print("Your number was lower than the answer, you need to go higher")