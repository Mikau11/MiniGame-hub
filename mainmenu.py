import star
import rpc
import bj
import hl
import Quiz
import corner


check = False

def menu():
    print("***Welcome to the Game/Activities menu***")
    print("   (1) Star")
    print("   (2) RockPaperScissors")
    print("   (3) BlackJack")
    print("   (4) Higher or Lower")
    print("   (5) Quiz")
    print("   (6) Sketchy Corner")
    wanna = int(input("Where do you wanna go?"))
    train(wanna, star.star, rpc.rockpaperscisors, bj.blackjack, hl.higher_lower, Quiz.quiz_operator, corner.conversation, corner.leave)
def train(station, func1, func2, func3, func4, func5, func6a, func6b):
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
        if not check:
            corner_check()
            func6a()
        elif check:
            func6b()
    else:
        print("There is no game here")
        menu()
def corner_check(): #I HATE that this is needed, because it does ONE thing and NOTHING else, but it DOESN'T WORK OTHERWISE
    global check
    check = True