def UserInputToList(x):
    user_list = x.split(" ")
    return user_list

def PutFetchLogic(x,lib):
    if x[0] == "put":
        lib[x[1]] = x[2]
        return lib
    elif x[0] == "fetch":
        value = lib.get(x[1], "Values not found.")
        print(value)
        return value