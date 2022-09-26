#!/usr/bin/python
import user_input

user_storage = {}
run = True

while run == True:
    string_input = input("> ")
    user_list = user_input.UserInputToList(string_input)

    if (user_list[0] == "put" and (len(user_list) > 3 or len(user_list) < 3)) or (user_list[0] == "fetch" and (len(user_list) > 2 or len(user_list) < 2)) or (user_list[0] == "exit" and len(user_list) > 1):
        print("Invalid syntax.")
    else:
        if user_list[0] == "put":
            user_input.PutLogic(user_list, user_storage)
            print("Ok.")
        elif user_list[0] == "fetch":
            user_input.FetchLogic(user_list, user_storage)
        elif user_list[0] == "exit":
            print("Bye!")
            run = False
        else:
            print('Unknown command. Known commands are: "put", "fetch", "exit".')
