message = input()
command = input()
decoded_message = ''


def insert_func(parameters):
    index = int(parameters[1])
    value = parameters[2]
    result = ''
    result += message[0:index] + value + message[index:]
    return result


while command != "Decode":
    parameters = command.split("|")
    if parameters[0] == "Move":
        num_letters = int(parameters[1])
        decoded_message = message[num_letters:]
        decoded_message += message[0:num_letters]
        message = decoded_message
    if parameters[0] == "Insert":
        decoded_message = insert_func(parameters)
        message = decoded_message
    if parameters[0] == "ChangeAll":
        substring = parameters[1]
        replacement = parameters[2]
        result = message.replace(substring, replacement)
        decoded_message = result
        message = decoded_message
    command = input()


print(f"The decrypted message is: {decoded_message}")
