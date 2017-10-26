import json

userName = input("What is your name? ")

fileName = "username.json"

with open(fileName, "w") as fileObject:
    json.dump(userName, fileObject)