def UserInputToList(x): #For taking and splitting user input into a list
    user_list = x.split(" ")
    return user_list

def PutLogic(list,dictionary): #Logic for putting key/values into the dictionary
    dictionary[list[1]] = list[2]
    return dictionary

def FetchLogic(list,dictionary): #Logic for fetching values based on the key
    value = dictionary.get(list[1], "Value not found.")
    print(value)