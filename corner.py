import mainmenu

def check():
    print("I thought I told you to SCRAM")
def conversation():
    print("Hey kid, wanna know a secret?")
    print("**Y/N**")
    s = input()
    if s == "N":
        print("Then Scram")
        mainmenu.menu()
    if s == "n":
        print("Then Scram")
        mainmenu.menu()
    print("When a Y/N option pops up, anything other than N or n means yes, probably because the programmer was lazy")
    print("Now Scram")
    print("**Y/N**")
    yn = input()
    if yn == "N":
        print("I said SCRAM")
    if yn == "n":
        print("I said SCRAM") #uhoh
    mainmenu.menu()
