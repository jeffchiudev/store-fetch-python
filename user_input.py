def UserInputToList(x):
    user_list = x.split(" ")
    return user_list

def PutLogic(x,dictionary):
    dictionary[x[1]] = x[2]
    return dictionary

def FetchLogic(x,dictionary):
    value = dictionary.get(x[1], "Values not found.")
    print(value)
