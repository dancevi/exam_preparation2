party_dict = dict()

disliked_counter = 0

command = input()

while command != "Stop":
    action = command.split("-")
    if action[0] == "Like":
        guest = action[1]
        meal = action[2]
        if guest not in party_dict.keys():
            party_dict[guest] = [meal]
        else:
            if meal not in party_dict[guest]:
                party_dict[guest].append(meal)

    elif action[0] == "Dislike":
        guest = action[1]
        meal = action[2]

        if guest not in party_dict:
            print(f"{guest} is not at the party.")
        else:
            if meal not in party_dict[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                party_dict[guest].remove(meal)
                disliked_counter += 1
    command = input()

for person in party_dict:
    print(f"{person}: {', '.join(party_dict[person])}")

print(f"Unliked meals: {disliked_counter}")