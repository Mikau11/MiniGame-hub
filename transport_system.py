def train(ticket, stay, go): #used at the end of the games to see where the user is going, ticket is the variable, which is inserted in each script(mostly ticketmachine)
    if ticket == 1:          #stay is the function of the game, eg rockpaperscissors, which calls the function again to play again
        stay()
    elif ticket == 2:       #stay calls the main menu function which is inserted in each script
        go()

def wrong_platform_check(check, go):
    if check == "N":
        go()
    if check == "n":
        go()