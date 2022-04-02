def add_func(command_split):
    song = command_split[1]
    performer = command_split[2]
    way = command_split[3]

    if song in my_dict.keys():
        return f"{song} is already in the collection!"
    else:
        my_dict[song] = [performer, way]
        return f"{song} by {performer} in {way} added to the collection!"


def remove_func(command_split):
    song = command_split[1]
    if song in my_dict.keys():
        my_dict.pop(song)
        return f"Successfully removed {song}!"
    else:
        return f"Invalid operation! {song} does not exist in the collection."


def change_key_func(command_split):
    song = command_split[1]
    way = command_split[2]
    if song in my_dict.keys():
        my_dict[song][1] = way
        return f"Changed the key of {song} to {way}!"
    else:
        return f"Invalid operation! {song} does not exist in the collection."

iterations = int(input())

my_dict = dict()

for _ in range(iterations):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    my_dict[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break

    command_split = command.split("|")
    if "Add" in command_split:
        print(add_func(command_split))
    if "Remove" in command_split:
        print(remove_func(command_split))
    if "ChangeKey" in command_split:
        print(change_key_func(command_split))

for k in my_dict:
    print(f"{k} -> Composer: {my_dict[k][0]}, Key: {my_dict[k][1]}")