realpassword = "1234"

def password():
    password = input("Enter password exactly: ")
    attempts = 1

    while password != realpassword:
        print("Password doesn't match")
        print("Hint: Incremental Numbers")
        password = input("Enter password exactly: ")
        attempts += 1
        if attempts > 4:
            print("Look, the password is 1234")
    print("It took you", attempts, "attempt(s)")
    print("Password match")