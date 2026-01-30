import transport_system

def star():
    print("***Star Rows***")
    transport_system.wrong_platform_check()
    print("First, How many stars do you want on each row?")
    num = int(input())
    print("Now, How many rows do you want?")
    rows = int(input())
    for x in range(rows):
        print("*" * num)
    transport_system.train(star) #See comment in transport_system.py

