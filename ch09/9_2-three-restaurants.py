# Define a class to represent a restaurant
import re


class Restaurant:
    """Simple class for representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describe the restaurant's attributes"""
        print(f"Welcome to {self.name}, home of the best "
            f"{self.cuisine_type} food around!")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

# Create three instances of the Restaurant class
restaurant1 = Restaurant("Tyler's Roadhouse", 'BBQ')
restaurant2 = Restaurant("Zinfandel Nightlight", "wine and cheese")
restaurant3 = Restaurant("Pizza Lola", 'pizza')

# Describe each restaurant
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
