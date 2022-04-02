import re

line = input()

my_dict = dict()

expression = r"(?P<symbol>[#|])(?P<food>[A-Z\sa-z]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"

matches = re.finditer(expression, line)
total_calories = 0
food_list = []
dates_list = []
calories_list = []

for match in matches:
    food = match.group("food")
    date = match.group("date")
    calories = int(match.group("calories"))
    total_calories += calories
    food_list.append(food)
    dates_list.append(date)
    calories_list.append(calories)


days_left = int(total_calories / 2000)

print(f"You have food to last you for: {days_left} days!")

if len(food_list) > 0:
    for n in range(len(food_list)):
        print(f"Item: {food_list[n]}, Best before: {dates_list[n]}, Nutrition: {calories_list[n]}")