magicians = ["alice", "david", "carolina"]

print("\n# 01")

for magician in magicians:
    print(magician)


print("\n# 02")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")


print("\n# 03")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Than you, everyone. That was a great magic show!")


print("\n# 04")

data = range(1, 5)
for value in data:
    print(value)
print(data)

print("\n# 05")

data = list(range(1, 6))
for value in data:
    print(value)
print(data)


print("\n# 06")

data = list(range(1, 11, 2))
for value in data:
    print(value)
print(data)


print("\n# 07")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


print("\n# 08")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


print("\n# 09")

squares = [value ** 2 for value in range(1, 11)]
print(squares)

squares = [value for value in range(1, 20)]
print(squares)


print("\n# 10")

players = ["charles", "martina", "michael", "florence", "eli"]

print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[1:])
print(players[-2:])

print("\n# 11")
for value in players[2:5]:
    print(value)


print("\n# 12")

my_foods = ["pizza", "falafel", "carrot cake"]

friend_foods = my_foods[:]

my_foods.append("cannoli")

friend_foods.append("ice cream")

print(my_foods)
print(friend_foods)


print("\n# 13")

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])


print("\n# 14")

dimensions = (400, 110, 23)
for value in dimensions:
    print(value)


