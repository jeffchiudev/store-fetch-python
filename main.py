import string
import user_input
user_storage = {}

run = True

while run == True:
    string_input = input("> ")
    user_list = user_input.UserInputToList(string_input)
    print(user_list)

    if user_list[0] == "put":
        user_input.PutLogic(user_list, user_storage)
    elif user_list[0] == "fetch":
        user_input.FetchLogic(user_list, user_storage)
    elif user_list[0] == "exit":
        print("Bye!")
        run = False


    print(user_storage)
