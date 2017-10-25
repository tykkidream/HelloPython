print("\n# 01")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


print("\n# 02")

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())

    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print("\n# 03")

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)


print("\n# 04")

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is you name? ")

    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no) ")

    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")