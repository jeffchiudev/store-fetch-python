def UserInputToList(x):
    user_list = x.split(" ")
    return user_list

def PutLogic(list,dictionary):
    dictionary[list[1]] = list[2]
    return dictionary

def FetchLogic(list,dictionary):
    value = dictionary.get(list[1], "Value not found.")
    print(value)