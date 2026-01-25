import mainmenu

with open("file.txt", "r") as files:
    file_data = files.readlines()


def name_password():
    name_start = input("What do you want you name to be(any name changes will require a restart to take effect)?\n")
    print(name_start, ",", name_start, "cool name")
    file_data[1] = name_start, "\n"
    file_data[2] = "0\n"
    print("Okay,", name_start, "lets go!!!")

    with open("file.txt", "w") as files:
        for line in file_data:
            files.writelines(line)
    mainmenu.menu()