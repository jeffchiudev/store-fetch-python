import string
import user_input
user_storage = {}

run = True

while run == True:
    string_input = input("> ")
    user_list = user_input.UserInputToList(string_input)
    # print(user_list)
    