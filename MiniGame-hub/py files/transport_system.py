import mainmenu

def train(stay):
    print("What do you wanna do?")
    print("(1) Play again")
    print("(2) Go back to main menu")
    ticketmachine = int(input())
    #used at the end of the games to see where the user is going, ticket is the variable, which is inserted in each script(mostly ticketmachine)
    if ticketmachine == 1:          #stay is the function of the game, eg rockpaperscissors, which calls the function again to play again
        stay()
    elif ticketmachine == 2:       #stay calls the main menu function which is inserted in each script
        mainmenu.menu()
    else:
        print("Gonna assume you meant to leave")
        mainmenu.menu()

def wrong_platform_check():
    print(" **Play?**")
    print(" **Y/N**") #same as the one further down
    play = input()
    if play == "N":
        mainmenu.menu()
    if play == "n":
        mainmenu.menu()