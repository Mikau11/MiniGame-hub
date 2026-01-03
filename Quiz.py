import random
import transport_system

def quiz_operator():
    print("***Quiz***")
    transport_system.wrong_platform_check()
    q1_chooser()
    q2_chooser()
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
        transport_system.train(quiz_operator)

def q1_b():
    print("(Q1) Whats the capital of England?")
    print("(1) Berlin")
    print("(2) Paris")
    print("(3) London")
    ans = int(input("Whats your answer?"))
    if ans != 3:
        print("Wrong!")
        transport_system.train(quiz_operator)


def q1_chooser():           #randomly chooses a function for q1
    q1 = random.randint(1, 2)
    if q1 == 1:
        q1_a()
    else:
        q1_b()

def q2_a():
    print("(Q2) Whats 1+1?")
    print("(1) 2")
    print("(2) 3")
    print("(3) 6")
    ans = int(input("Whats your answer?"))
    if ans != 1:
        print("Wrong!")
        transport_system.train(quiz_operator)
def q2_b():
    print("(Q2) Whats 2+1?")
    print("(1) 2")
    print("(2) 3")
    print("(3) 6")
    ans = int(input("Whats your answer?"))
    if ans != 2:
        print("Wrong!")
        transport_system.train(quiz_operator)

def q2_chooser():           #randomly chooses a function for q2
    q2 = random.randint(1, 2)
    if q2 == 1:
        q2_a()
    else:
        q2_b()

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
