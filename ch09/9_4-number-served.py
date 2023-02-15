# Class to represent a restaurant
import re


class Restaurant:
    """Simple class for representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe the restaurant's attributes"""
        print(f"Welcome to {self.name}, home of the best "
            f"{self.cuisine_type} food around!")

    def open_restaurant(self):
        """Print a notice that the restaurant is open"""
        print(f"{self.name} is now open.")
    
    def set_number_served(self, num):
        """Update the number_served attribute"""
        self.number_served = num
    
    def increment_number_served(self, add_num):
        """Increment the number_served attribute"""
        self.number_served += add_num

# Instances of the class Restaurant
restaurant_1 = Restaurant('Lolly Pops', 'Afro-Asian')

# Print out number served
restaurant_1.number_served = 24
print(restaurant_1.number_served)

# Use methods to update number served
restaurant_1.set_number_served(53)
print(restaurant_1.number_served)

restaurant_1.increment_number_served(157)
print(restaurant_1.number_served)
