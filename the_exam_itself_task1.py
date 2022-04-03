allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

initial_password = input()

command = input()


while command != "Complete":
    explode = command.split(" ")
    if explode[0] == "Make":
        index = int(explode[2])
        if explode[1] == "Upper":
            to_be_inserted = initial_password[index].upper()
            initial_password = initial_password[:index] + to_be_inserted + initial_password[index + 1:]
            print(initial_password)
        elif explode[1] == "Lower":
            to_be_inserted = initial_password[index].lower()
            initial_password = initial_password[:index] + to_be_inserted + initial_password[index + 1:]
            print(initial_password)

    elif explode[0] == "Insert":
        index = int(explode[1])
        char = explode[2]
        if index in range(len(initial_password)):
            initial_password = initial_password[:index] + char + initial_password[index:]
            print(initial_password)

    elif explode[0] == "Replace":
        char = explode[1]
        value = int(explode[2])
        if char in initial_password:
            new_char = chr(ord(char) + value)
            initial_password = initial_password.replace(char, new_char)
            print(initial_password)

    elif explode[0] == "Validation":
        if len(initial_password) < 8:
            print("Password must be at least 8 characters long!")

        for i in initial_password:
            if i not in allowed:
                print("Password must consist only of letters, digits and _!")
                break
        is_upper = False
        for j in initial_password:
            if j.isupper():
                is_upper = True
        if not is_upper:
            print("Password must consist at least one uppercase letter!")
        is_lower = False
        for h in initial_password:
            if h.islower():
                is_lower = True
        if not is_lower:
            print("Password must consist at least one lowercase letter!")

        is_digit = False
        for k in initial_password:
            if k.isdigit():
                is_digit = True
        if not is_digit:
            print("Password must consist at least one digit!")

    command = input()


