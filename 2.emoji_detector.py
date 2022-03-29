import re

text = input()

emoji_reg = r"([:]{2}|[*]{2})[A-Z][a-z]{2,}\1"
digits_reg = r'\d'

all_nums = re.findall(digits_reg, text)

cool_threshold = 1

for match in all_nums:
    cool_threshold *= int(match)

all_emoji = re.finditer(emoji_reg, text)
total_emoji_counter = 0
cool_emoji = []

for n in all_emoji:
    total_emoji_counter += 1
    word_sum = 0
    if "**" in n[0]:
        word = n[0].strip("**")
        for letter in word:
            word_sum += ord(letter)
    elif "::" in n[0]:
        word = n[0].strip("::")
        for letter in word:
            word_sum += ord(letter)

    if word_sum >= cool_threshold: # moje da e samo po golqmo
        cool_emoji.append(n[0])


print(f"Cool threshold: {cool_threshold}")
print(f"{total_emoji_counter} emojis found in the text. The cool ones are:")
for w in cool_emoji:
    print(w)

