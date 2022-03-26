import re

iterations = int(input())

my_list = []

expression = re.compile(r"^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$")

for _ in range(iterations):
    word = input()
    my_list.append(word)

filtered_list = [i for i in my_list if expression.match(i)]

print(filtered_list)





