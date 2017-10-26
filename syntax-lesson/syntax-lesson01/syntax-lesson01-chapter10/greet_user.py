import json

fileName = "username.json"

with open(fileName) as fileObject:
    username = json.load(fileObject)
    print(username)