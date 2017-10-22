bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

print(bicycles[0])

message = "my first bicycle was a " + bicycles[0].title() + "."

print(message)

motorcycles = ["honda", 'yamaha', "suzuki"]

print(motorcycles)

motorcycles[0] = "ducati"

print(motorcycles)

motorcycles.append("ducati")

print(motorcycles)

motorcycles.clear()

print(motorcycles)

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

print(motorcycles)

motorcycles.insert(1, "ducati")

print(motorcycles)

del motorcycles[1]

print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(popped_motorcycle)
print(motorcycles)


motorcycles = ["honda", 'yamaha', "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop(2)
print(popped_motorcycle)
print(motorcycles)



motorcycles = ["honda", 'yamaha', "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)



cars = ["bmw", "auid", "toyota", "subaru"]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


cars = ["bmw", "auid", "toyota", "subaru"]
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))


cars = ["bmw", "auid", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)

print(len(cars))