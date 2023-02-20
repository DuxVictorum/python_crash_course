# Classes
from re import M


class Car:
    """Represents a basic car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer, silly!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """Represents an electric car battery"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    # New method for 9_9 to upgrade your battery
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print(f"Congratulations, we've upgraded your battery to 100 kWh.")
        elif self.battery_size == 100:
            print("Your battery is already at the larger 100-kWh size.")


class ElectricCar(Car):
    """Represents an electric car; inherits Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Let's make an electric car instance
flashy = ElectricCar('Toyota', 'Corolla', 2025)

# Class methods
print(f"\nHow about buying a brand new {flashy.get_descriptive_name()}?")
flashy.read_odometer()
flashy.battery.describe_battery()
flashy.battery.get_range()

print("But wait, it seems you qualify for a battery upgrade!\n")
flashy.battery.upgrade_battery()
flashy.battery.get_range()
