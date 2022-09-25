def UserInputToList(x):
    user_list = x.split(" ")
    return user_list

def PutLogic(x,lib):
    if x[0] == "put":
        lib[x[1]] = x[2]
    return lib

