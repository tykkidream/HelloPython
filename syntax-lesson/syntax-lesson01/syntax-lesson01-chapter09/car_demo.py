from car import Car

my_new_car = Car("audi", "a4", 2016)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(46)
my_new_car.read_odometer()


my_new_car.update_odometer(45)

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.fill_gas_tamk()