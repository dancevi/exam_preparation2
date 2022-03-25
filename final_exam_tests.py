######## 1 Imitation Game
# message = input()
# command = input()
# decoded_message = ''
#
# def insert_func(parameters):
#     index = int(parameters[1])
#     value = parameters[2]
#     result = ''
#     result += message[0:index] + value + message[index:]
#     return result
#
#
#
#
#
# while command != "Decode":
#     parameters = command.split("|")
#     if parameters[0] == "Move":
#         num_letters = int(parameters[1])
#         decoded_message = message[num_letters:]
#         decoded_message += message[0:num_letters]
#         message = decoded_message
#     if parameters[0] == "Insert":
#         decoded_message = insert_func(parameters)
#         message = decoded_message
#     if parameters[0] == "ChangeAll":
#         substring = parameters[1]
#         replacement = parameters[2]
#         result = message.replace(substring, replacement)
#         decoded_message = result
#         message = decoded_message
#     command = input()
#
#
# print(f"The decrypted message is: {decoded_message}")


######### 2 Ad Astra

# import re
#
# line = input()
#
# my_dict = dict()
#
# expression = r"(?P<symbol>[#|])(?P<food>[A-Z\sa-z]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"
#
# matches = re.finditer(expression, line)
# total_calories = 0
# food_list = []
# dates_list = []
# calories_list = []
#
# for match in matches:
#     food = match.group("food")
#     date = match.group("date")
#     calories = int(match.group("calories"))
#     total_calories += calories
#     food_list.append(food)
#     dates_list.append(date)
#     calories_list.append(calories)
#
#
# days_left = int(total_calories / 2000)
#
# print(f"You have food to last you for: {days_left} days!")
#
# if len(food_list) > 0:
#     for n in range(len(food_list)):
#         print(f"Item: {food_list[n]}, Best before: {dates_list[n]}, Nutrition: {calories_list[n]}")

########### 3 THE PIANIST
# def add_func(command_split):
#     song = command_split[1]
#     performer = command_split[2]
#     way = command_split[3]
#
#     if song in my_dict.keys():
#         return f"{song} is already in the collection!"
#     else:
#         my_dict[song] = [performer, way]
#         return f"{song} by {performer} in {way} added to the collection!"
#
#
# def remove_func(command_split):
#     song = command_split[1]
#     if song in my_dict.keys():
#         my_dict.pop(song)
#         return f"Successfully removed {song}!"
#     else:
#         return f"Invalid operation! {song} does not exist in the collection."
#
#
# def change_key_func(command_split):
#     song = command_split[1]
#     way = command_split[2]
#     if song in my_dict.keys():
#         my_dict[song][1] = way
#         return f"Changed the key of {song} to {way}!"
#     else:
#         return f"Invalid operation! {song} does not exist in the collection."
#
# iterations = int(input())
#
# my_dict = dict()
#
# for _ in range(iterations):
#     data = input().split("|")
#     piece = data[0]
#     composer = data[1]
#     key = data[2]
#     my_dict[piece] = [composer, key]
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#
#     command_split = command.split("|")
#     if "Add" in command_split:
#         print(add_func(command_split))
#     if "Remove" in command_split:
#         print(remove_func(command_split))
#     if "ChangeKey" in command_split:
#         print(change_key_func(command_split))
#
# for k in my_dict:
#     print(f"{k} -> Composer: {my_dict[k][0]}, Key: {my_dict[k][1]}")


###############
#EXAM 2
###############
#1 WORLD TOUR

# initial_string = input()
# command = input()
#
# while command != "Travel":
#
#     inputs = command.split(":")
#     action = inputs[0]
#
#     if action == "Add Stop":
#         index = int(inputs[1])
#         place = inputs[2]
#         if index in range(len(initial_string)):
#             initial_string = initial_string[0:index] + place + initial_string[index:len(initial_string)]
#
#     elif action == "Remove Stop":
#         start_index = int(inputs[1])
#         end_index = int(inputs[2])
#         if start_index in range(len(initial_string)) and end_index in range(len(initial_string)):
#             initial_string = initial_string[0:start_index] + initial_string[end_index + 1:]
#     else:
#         old_str = inputs[1]
#         new_str = inputs[2]
#         initial_string = initial_string.replace(old_str, new_str)
#     print(initial_string)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {initial_string}")

#2 Destination Mapper

# import re
#
# text = input()
# expression = r"([=|/])(?P<City>[A-Z][a-zA-Z]{2,})\1"
#
# output = []
#
# matches = re.finditer(expression, text)
#
# for match in matches:
#     city = match.group("City")
#     output.append(city)
#
# travel_points = 0
#
# for c in output:
#     travel_points += len(c)
#
# print(f"Destinations: {', ' .join(output)}")
# print(f"Travel Points: {travel_points}")

#3 PLANT DISCOVERY


# iterations = int(input())
# plant_dict = dict()
#
# for _ in range(iterations):
#     items = input().split("<->")
#     plant = items[0]
#     rarity = items[1]
#
#     plant_dict[plant] = [rarity]
#
# command = input()
#
# while command != "Exhibition":
#     command = command.split(":")
#     if command[0] == "Rate":
#         actions = command[1].split("-")
#         plant_name = actions[0].strip()
#         rating = actions[1].strip()
#         if plant_name in plant_dict.keys():
#             plant_dict[plant_name].append(rating)
#         else:
#             print("error")
#     elif command[0] == "Update":
#         actions = command[1].split("-")
#         plant_name = actions[0].strip()
#         new_rarity = actions[1].strip()
#         if plant_name in plant_dict.keys():
#             plant_dict[plant_name][0] = new_rarity
#         else:
#             print("error")
#     elif command[0] == "Reset":
#         plant_name = command[1].strip()
#         if plant_name in plant_dict.keys():
#             plant_dict[plant_name] = [plant_dict[plant_name][0]]
#         else:
#             print("error")
#
#     command = input()
#
#
# print("Plants for the exhibition:")
# for key in plant_dict:
#     total_rating = 0
#     average_rating = 0
#     final_rarity = plant_dict[key].pop(0)
#     if len(plant_dict[key]) > 0:
#         for rating in plant_dict[key]:
#             total_rating += int(rating)
#         average_rating = total_rating / len(plant_dict[key])
#     print(f"- {key}; Rarity: {final_rarity}; Rating: {average_rating:.2f}")


##################
# EXAM3
##################

##### 1 SECRET CHAT
# concealed_msg = input()
#
# command = input()
#
# while command != "Reveal":
#     isthere = True
#     data = command.split(":|:")
#     action = data[0]
#
#     if action == "InsertSpace":
#         index = int(data[1])
#         concealed_msg = concealed_msg[0:index] + " " + concealed_msg[index:len(concealed_msg)]
#     elif action == "Reverse":
#         substring = data[1]
#
#         if substring in concealed_msg:
#             concealed_msg = concealed_msg.replace(substring, "", 1)
#             substring = substring[::-1]
#             concealed_msg += substring
#         else:
#             isthere = False
#             print("error")
#     else:
#         substring = data[1]
#         replacement = data[2]
#         concealed_msg = concealed_msg.replace(substring, replacement)
#     if isthere:
#         print(concealed_msg)
#     command = input()
#
# print(f"You have a new text message: {concealed_msg}")

###### 2 Mirror Words
# import re
#
# text = input()
# expression = r"([#|@])[a-zA-Z]{3,}\1{2}[a-zA-Z]{3,}\1"
#
# my_list = []
#
# matches = re.finditer(expression, text)
#
# for match in matches:
#     my_list.append(match.group())
#
# if len(my_list) > 0:
#     print(f"{len(my_list)} word pairs found!")
# else:
#     print("No word pairs found!")
#
# mirrors_dict = {}
#
# for item in my_list:
#     first_half = item[1:int(len(item)/2) - 1]
#     second_half = item[int(len(item)/2)+1:len(item) - 1]
#     if first_half == second_half[::-1]:
#         mirrors_dict[first_half] = second_half
#
# final_list = []
# for key in mirrors_dict:
#     working_str = ""
#     working_str += f"{key} <=> {mirrors_dict[key]}"
#     final_list.append(working_str)
#
#
# if len(final_list) > 0:
#     print("The mirror words are:")
#     print(", ".join(final_list))
# else:
#     print("No mirror words!")

# cars_dict[car_name][1] + refuel < 75

####### 3 NEED FOR SPEED III
# def drive_car(data):
#     car_name = data[1]
#     distance = int(data[2])
#     consumed = int(data[3])
#     if cars_dict[car_name][1] < consumed:
#         print("Not enough fuel to make that ride")
#     else:
#         cars_dict[car_name][0] += distance
#         cars_dict[car_name][1] -= consumed
#         print(f"{car_name} driven for {distance} kilometers. {consumed} liters of fuel consumed.")
#     if cars_dict[car_name][0] >= 100000: #COULD BE INTEGRATED IN THE ELSE ABOVE
#         del cars_dict[car_name]
#         print(f"Time to sell the {car_name}!")
#
#
# def refuel_car(data):
#     car_name = data[1]
#     refuel = int(data[2])
#     litres = 0
#     if cars_dict[car_name][1] <= 75:#MAYBE NEED OF AN ELSE
#         if cars_dict[car_name][1] + refuel >= 75:
#             litres = 75 - cars_dict[car_name][1]
#             cars_dict[car_name][1] = 75 # TUK MOJE DA IMA GRESHKA
#         else: # CAN ALSO BE ONLY ELSE
#             cars_dict[car_name][1] = cars_dict[car_name][1] + refuel
#             litres = refuel
#     print(f"{car_name} refueled with {litres} liters")
#
#
# def revert_car(data):
#     car_name = data[1]
#     kilometers = int(data[2])
#     if cars_dict[car_name][0] - kilometers < 10000:
#         cars_dict[car_name][0] = 10000
#     else:
#         cars_dict[car_name][0] = cars_dict[car_name][0] - kilometers
#         print(f"{car_name} mileage decreased by {kilometers} kilometers")
#
#
#
# num_of_cars = int(input())
# cars_dict = dict()
#
# for _ in range(num_of_cars):
#     car_data = input().split("|")
#     car_make = car_data[0]
#     mileage = int(car_data[1])
#     fuel = int(car_data[2])
#
#     cars_dict[car_make] = [mileage, fuel]
#
# command = input()
#
# while command != "Stop":
#
#     data = command.split(" : ")
#
#     if data[0] == "Drive":
#         drive_car(data)
#
#     elif data[0] == "Refuel":
#         refuel_car(data)
#
#     else:
#         revert_car(data)
#     command = input()
#
# for key in cars_dict:
#     print(f"{key} -> Mileage: {cars_dict[key][0]} kms, Fuel in the tank: {cars_dict[key][1]} lt.")


#####################
#EXAM 4
#####################

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