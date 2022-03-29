init_input = input()

command = input()

while command != "Generate":
    actions = command.split(">>>")

    if actions[0] == "Contains":
        pass
    elif actions[0] == "Flip":
        pass
    elif actions[0] == "Slice":
        pass

    command = input()