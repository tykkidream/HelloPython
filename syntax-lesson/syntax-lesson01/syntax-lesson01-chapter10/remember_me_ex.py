import json

def greet_user():
    fileName = "username.json"

    try:
        with open(fileName) as fileObject:
            username = json.load(fileObject)
    except FileNotFoundError:
        userName = input("What is your name? ")

        with open(fileName, "w") as fileObject:
            json.dump(userName, fileObject)
    else:
        print("Welcom back, " + username + "!")


greet_user()





def get_stored_username():
    fileName = "username.json"

    try:
        with open(fileName) as fileObject:
            username = json.load(fileObject)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    fileName = "username.json"

    userName = input("What is your name? ")

    with open(fileName, "w") as fileObject:
        json.dump(userName, fileObject)

    return userName


def greet_user_ex():
    username = get_stored_username()

    if username:
        print("Welcom back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you wehn you com back, " + username + "!")


greet_user_ex()