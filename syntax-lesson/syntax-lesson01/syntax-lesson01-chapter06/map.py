print("\n# 01")

alien_0 = { "color" : "green", "points" : 5}

print(alien_0["color"])
print(alien_0["points"])



print("\n# 02")

alien_0 = { "color" : "green", "points" : 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)


print("\n# 03")

alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5

print(alien_0)

alien_0["color"] = "yellow"
print(alien_0)


print("\n# 04")

alien_0 = {"x_position" : 0, "y_position": 25, "speed" : "medium"}

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(alien_0["x_position"])


print("\n# 05")

print(alien_0)
del alien_0["x_position"]
print(alien_0)


print("\n# 06")

favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python"
}

print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages["sarah"].title() + ".")


print("\n# 07")

user_0 = {
    "username" : "efermi",
    "first" : "enrico",
    "last" : "fermi"
}

for key, value in user_0.items():
    print("\nkey: " + key)
    print("value: " + value)


print("\n# 08")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


print("\n# 09")

for name in favorite_languages.keys():
    print(name.title())


print("\n# 10")

friends = ["phil", "sarah"]
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print("    Hi " + name.title() + ", I see your favorie language is " + favorite_languages[name].title() + "!")


print("\n# 11")

data = favorite_languages.keys();
print(data)
if "erin" not in data:
    print("Eri, please take our poll!")


print("\n# 12")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the pool.")


print("\n# 13")

for language in favorite_languages.values():
    print(language)

print()

for language in set(favorite_languages.values()):
    print(language)


print("\n# 14")

alien_0 = {"color" : "green", "points" : 5}
alien_1 = {"color" : "yellow", "points" : 10}
alien_2 = {"color" : "red", "points" : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


print("\n# 15")

aliens = []

for alien_number in range(30):
    new_alien = {"color" : "green", "points" : alien_number, "speed" : "slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print("Total number of aliens:" + str(len((aliens))))


print("\n# 16")

for alien in aliens[:3]:
    alien["color"] = "yellow"
    alien["speed"] = "medium"
    alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
print("...")


print("\n# 17")

pizza = {
    "crust" : "thick",
    "toppings" : ["mushrooms", "extra cheese"]
}

print("You ordered a " + pizza["crust"] + "-crust pizza " + "with the following toppings:")

for toppings in pizza["toppings"]:
    print("\t" + toppings)


print("\n# 18")

favorite_languages = {
    "jen" : ["python", "ruby"],
    "sarah" : ["c"],
    "edward" : ["ruby", "go"],
    "phil": ["python", "haskell"]
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


print("\n# 19")

users = {
    "aeinstein" : {
        "first" : "albert",
        "last" : "einstein",
        "location" : "princeton"
    },
    "mcurie" : {
        "first" : "marie",
        "last" : "curie",
        "location" : "paris"
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())