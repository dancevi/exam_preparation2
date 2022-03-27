def cast_spell(data):
    h_name = data[1]
    mp_needed = int(data[2])
    spell_name = data[3]
    if h_name in hero_information.keys():
        if hero_information[h_name][1] >= mp_needed:
            hero_information[h_name][1] -= mp_needed
            print(f"{h_name} has successfully cast {spell_name} and now has {hero_information[h_name][1]} MP!")
        else:
            print(f"{h_name} does not have enough MP to cast {spell_name}!")


def take_damage(data):
    h_name = data[1]
    damage = int(data[2])
    attacker = data[3]
    hero_information[h_name][0] = hero_information[h_name][0] - damage
    if hero_information[h_name][0] > 0:
        print(f"{h_name} was hit for {damage} HP by {attacker} and now has {hero_information[h_name][0]} HP left!")
    else:
        del hero_information[h_name]
        print(f"{h_name} has been killed by {attacker}!")


def recharge(data):
    h_name = data[1]
    amount = int(data[2])

    if hero_information[h_name][1] + amount > 200:
        amount = 200 - hero_information[h_name][1]
        hero_information[h_name][1] = 200
    else:
        hero_information[h_name][1] += amount
    print(f"{h_name} recharged for {amount} MP!")


def heal(data):
    h_name = data[1]
    amount = int(data[2])

    if hero_information[h_name][0] + amount > 100:
        amount = 100 - hero_information[h_name][0]
        hero_information[h_name][0] = 100
    else:
        hero_information[h_name][0] += amount
    print(f"{h_name} healed for {amount} HP!")


iterations = int(input())

hero_information = dict()

for _ in range(iterations):
    stats = input().split(" ")
    name = stats[0]
    hp = int(stats[1])
    mp = int(stats[2])
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    if name not in hero_information.keys():
        hero_information[name] = [hp, mp]

command = input()

while command != "End":
    actions = command.split(" - ")
    if actions[0] == "CastSpell":
        cast_spell(actions)
    elif actions[0] == "TakeDamage":
        take_damage(actions)
    elif actions[0] == "Recharge":
        recharge(actions)
    elif actions[0] == "Heal":
        heal(actions)

    command = input()


for hero in hero_information:
    print(f"{hero}")
    print(f"  HP: {hero_information[hero][0]}")
    print(f"  MP: {hero_information[hero][1]}")