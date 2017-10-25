print("\n# 01")

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1


print("\n# 02")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end to program. "

message = ""
while message != "quit":
    message = input(prompt)
    print(message)


print("\n# 03")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end to program. "

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)


print("\n# 04")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end to program. "

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)


print("\n# 05")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print("I'd love to go to " + message.title() + "!")

