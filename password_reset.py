initial_password = input()

command = input()

while command != "Done":
    explode = command.split(" ")
    if explode[0] == "TakeOdd":
        new_str = ""
        for i in range(1, len(initial_password), 2):
            new_str += initial_password[i]
        initial_password = new_str
        print(initial_password)
    elif explode[0] == "Cut":
        index = int(explode[1])
        length = int(explode[2])
        the_cut = initial_password[index: index + (length)]
        initial_password = initial_password.replace(the_cut, "", 1)
        print(initial_password)
    else:
        substring = explode[1]
        substitute = explode[2]
        if substring in initial_password:
            initial_password = initial_password.replace(substring, substitute)
            print(initial_password)
        else:
            print("Nothing to replace!")

    command = input()


print(f"Your password is: {initial_password}")