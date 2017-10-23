print("\n# 01")

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


print("\n# 02")

car = "Audit"
print(car == "audit")
print(car != "audit")
print(car.lower() == "audit")


print("\n# 03")

age = 18
print(age == 18)
print(age == 19)
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


print("\n# 04")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))


print("\n# 05")

requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)


print("\n# 06")

banned_users = ["andrew", "carolina", "david"]
print("marie" not in banned_users)


print("\n# 07")

game_active = True
print(game_active)


print("\n# 08")

age = 17

if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young t vote.")
    print("Please register to vote as soon as you turn 18!")


print("\n# 09")

age = 12
if age < 4:
    print("YOur admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")


print("\n# 10")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+ requested_topping + ".")
print("\nFinished making your pizza!")


print("\n# 11")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping + ".")
    print("\nFinished making your pizza!")
print("Are you sure you want a plain pizza?")


print("\n# 12")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+ requested_topping + ".")
    else:
        print("Sorry, we are out of green peppers right now.")
print("\nFinished making your pizza!")

