import mainmenu
import transport_system
import rpc
def star():
    print("***Star Rows***")
    print(" **Play?**")
    print(" **Y/N**") #same as the one further down
    p = input() #but done exclusivley for the beginging
    transport_system.wrong_platform_check(p, mainmenu.menu) #because its done barely differently
    print("First, How many stars do you want on each row?")
    num = int(input())
    print("Now, How many rows do you want?")
    rows = int(input())
    for x in range(rows):
        print("*" * num)
    print("What do you wanna do?")
    print("(1) Play again")
    print("(2) Go back to main menu")
    ticketmachine = int(input()) #Asks the user where they wanna go
    transport_system.train(ticketmachine, star, mainmenu.menu) #See comment in transport_system.py

