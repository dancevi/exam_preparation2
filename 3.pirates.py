targeted_cities = dict()

command = input()

while command != "Sail":
    data = command.split("||")
    name = data[0]
    population = int(data[1])
    gold = int(data[2])

    if name not in targeted_cities.keys():
        targeted_cities[name] = [population, gold]
    else:
        targeted_cities[name][0] += population
        targeted_cities[name][1] += gold
    command = input()



events = input()

while events != "End":
    actions = events.split("=>")
    if actions[0] == "Plunder":
        town = actions[1]
        people = int(actions[2])
        xau = int(actions[3])
        targeted_cities[town][0] -= people
        targeted_cities[town][1] -= xau
        print(f"{town} plundered! {xau} gold stolen, {people} citizens killed.")

        if targeted_cities[town][0] == 0 or targeted_cities[town][1] == 0:
            targeted_cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif actions[0] == "Prosper":
        town = actions[1]
        xau = int(actions[2])
        if xau >= 0:
            targeted_cities[town][1] += xau
            print(f"{xau} gold added to the city treasury. {town} now has {targeted_cities[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    events = input()


if len(targeted_cities) > 0:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")

    for city in targeted_cities:
        print(f"{city} -> Population: {targeted_cities[city][0]} citizens, Gold: {targeted_cities[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")