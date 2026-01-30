import random
import transport_system


def quiz_operator():
    print("***Quiz***")
    transport_system.wrong_platform_check()
    print("############")
    print("#Question 1#")
    print("############")
    q1_chooser()
    print("############")
    print("#Question 2#")
    print("############")
    q2_chooser()
    print("############")
    print("#Question 3#")
    print("############")
    q3_chooser()
    transport_system.train(quiz_operator)


def q1_a():
    print("(Q1) Whats the capital of France?")
    print("(1) Berlin")
    print("(2) Paris")
    print("(3) Vienna")
    ans = int(input("Whats your answer?"))
    if ans != 2:
        print("Wrong!")
        applicable_answer(ans)
def q1_b():
    print("(Q1) Whats the capital of England?")
    print("(1) Tokyo")
    print("(2) Sao Paulo")
    print("(3) London")
    ans = int(input("Whats your answer?"))
    if ans != 3:
        print("Wrong!")
        applicable_answer(ans)


def q1_c():
    print("(Q1) Whats the capital of Russia?")
    print("(1) Moscow")
    print("(2) Canberra")
    print("(3) Ottawa")
    ans = int(input("Whats your answer?"))
    if ans != 1:
        print("Wrong!")
        applicable_answer(ans)


def q1_d():
    print("(Q1) What are the only 2 countries that can legally take parts of antarctica?")
    print("(1) USA and Russia")
    print("(2) Germany and Canada")
    print("(3) France and Japan")
    ans = int(input("Whats your answer?"))
    if ans != 1:
        print("Wrong!")
        applicable_answer(ans)


def q1_e():
    print("(Q1) What is the Biggest landmass?")
    print("(1) The Americas")
    print("(2) Antarctica")
    print("(3) Eurasia")
    ans = int(input("Whats your answer?"))
    if ans != 3:
        print("Wrong!")
        if ans > 3:
            applicable_answer(ans)

def q1_chooser():           #randomly chooses a function for q1
    q1 = random.randint(1, 5)
    if q1 == 1:
        q1_a()
    elif q1 == 2:
        q1_b()
    elif q1 == 3:
        q1_c()
    elif q1 == 4:
        q1_d()
    else:
        q1_e()

def q2_a():
    print("(Q2) What is +- equivalent to?")
    print("(1) Add")
    print("(2) Subtract")
    print("(3) Divide")
    ans = int(input("Whats your answer?"))
    if ans != 2:
        print("Wrong!")
        if ans > 3:
            applicable_answer(ans)
        transport_system.train(quiz_operator)
def q2_b():
    print("(Q2) What is -- equivalent to?")
    print("(1) Add")
    print("(2) Subtract")
    print("(3) Divide")
    ans = int(input("Whats your answer?"))
    if ans != 1:
        print("Wrong!")
        if ans > 3:
            applicable_answer(ans)
        transport_system.train(quiz_operator)

def q2_c():
    print("(Q2) How do you go about squaring a negative number?")
    print("(1) -(a * a)")
    print("(2) (-a) * (-a)")
    print("(3) (-a) * (a)")
    ans = int(input("Whats your answer?"))
    if ans != 2:
        print("Wrong!")
        if ans > 3:
            applicable_answer(ans)
        transport_system.train(quiz_operator)


def q2_d():
    print("(Q2) Given that a = -2, and b = -4, whats b/a?")
    print("(1) 2")
    print("(2) 1.5")
    print("(3) 0.5")
    ans = int(input("Whats your answer?"))
    if ans != 3:
        print("Wrong!")
        if ans > 3:
            applicable_answer(ans)
        transport_system.train(quiz_operator)


def q2_chooser():           #randomly chooses a function for q2
    q2 = random.randint(1, 4)
    if q2 == 1:
        q2_a()
    elif q2 == 2:
        q2_b()
    elif q2 == 3:
        q2_c()
    else:
        q2_d()

def q3_a():
    print("(Q3) Whats5*5?")
    print("(1) 2")
    print("(2) 3")
    print("(3) 25")
    ans = int(input("Whats your answer?"))
    if ans != 3:
        print("Wrong!")
        transport_system.train(quiz_operator)

def q3_b():
    print("(Q3) Whats 5*6?")
    print("(1) 2")
    print("(2) 30")
    print("(3) 6")
    ans = int(input("Whats your answer?"))
    if ans != 2:
        print("Wrong!")
        transport_system.train(quiz_operator)


def q3_chooser():           #randomly chooses a function for q3
    q3 = random.randint(1, 2)
    if q3 == 1:
        q3_a()
    else:
        q3_b()


def applicable_answer(answer):
    if answer > 3:
        print("You didn't even pick an applicable answer......")
    transport_system.train(quiz_operator)