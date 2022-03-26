import re

iterations = int(input())

my_list = []

expression = re.compile(r"^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$")

for _ in range(iterations):
    word = input()
    if expression.match(word):
        product_group = ""
        for letter in word:
            if letter.isnumeric():
                product_group += letter
        if len(product_group) == 0:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")




#Adding a test here




