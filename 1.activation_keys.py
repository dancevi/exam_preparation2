init_input = input()

command = input()

while command != "Generate":
    actions = command.split(">>>")

    if actions[0] == "Contains":
        if actions[1] in init_input:
            print(f"{init_input} contains {actions[1]}")
        else:
            print("Substring not found!")
    elif actions[0] == "Flip":
        start = int(actions[2])
        end = int(actions[3])
        the_cut = init_input[start: end]
        if actions[1] == "Upper":
            init_input = init_input[0:start] + the_cut.upper() + init_input[end:]
        elif actions[1] == "Lower":
            init_input = init_input[0:start] + the_cut.lower() + init_input[end:]
        print(init_input)
    elif actions[0] == "Slice":
        start = int(actions[1])
        end = int(actions[2])
        init_input = init_input[0:start] + init_input[end:]
        print(init_input)
    command = input()

print(f"Your activation key is: {init_input}")