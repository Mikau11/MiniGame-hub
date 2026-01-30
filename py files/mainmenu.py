import star
import rpc
import bj
import hl
import Quiz
import corner
import thefiles
import name


check = False

def menu():
    with open("other files/file.txt", "r") as files:
        file_data = files.readlines()
    print("Hello," + file_data[1] + "!!!!")
    print("***Welcome to the Game/Activities menu***")
    print("   (1) Star")
    print("   (2) RockPaperScissors")
    print("   (3) BlackJack")
    print("   (4) Higher or Lower")
    print("   (5) Quiz")
    print("   (6) Settings")
    print("   (7) Sketchy Corner")
    wanna = int(input("Where do you wanna go?"))
    train(wanna, star.star, rpc.rockpaperscisors, bj.blackjack, hl.higher_lower, Quiz.quiz_operator, name.name_password, corner.conversation, corner.leave)
def train(station, func1, func2, func3, func4, func5, func6, func7a, func7b):
    if station == 1:
        func1()
    elif station == 2:
        func2()
    elif station == 3:
        func3()
    elif station == 4:
        func4()
    elif station == 5:
        func5()
    elif station == 6:
        func6()
    elif station == 7:
        if not check:
            corner_check()
            func7a()
        elif check:
            func7b()
    else:
        print("There is no game here")
        menu()
def corner_check(): #I HATE that this is needed, because it does ONE thing and NOTHING else, but it DOESN'T WORK OTHERWISE
    global check
    check = True