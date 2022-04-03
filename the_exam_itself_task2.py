import re

iterations = int(input())

correct_str_check = r"^(![A-Z][a-z]{2,}!):(\[[A-Za-z]{8,}\])$"

for _ in range(iterations):
    string = input()
    if re.match(correct_str_check, string):
        my_list = re.finditer(correct_str_check, string)
        for match in my_list:
            command = match[1].strip("!")
            word = match[2]
            final_word = word[1:-1]
            code_list = [str(ord(l)) for l in final_word]

            print(f"{command}: {' '.join(code_list)}")

    else:
        print("The message is invalid")
