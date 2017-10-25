from car import Car
from battery import Battery

class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("THis car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tamk(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

