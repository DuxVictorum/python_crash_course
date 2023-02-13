# Gettin' classy -- Create a class for a sample restaurant
class Restaurant:
    """Simple class for representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.sign = "Put some pork on your fork"
    
    def describe_restaurant(self):
        """Describe the restaurant's attributes"""
        print(f"Welcome to {self.name}, home of the best "
            f"{self.cuisine_type} food around!")
        print(f"As the sign says, {self.sign}.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

# Create an instance of Restaurant
waffle_house = Restaurant("Waffle House", "classic American diner")

# Test the attributes and methods
print(waffle_house.cuisine_type)

waffle_house.describe_restaurant()

waffle_house.open_restaurant()