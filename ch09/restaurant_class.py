# Parent class
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
        """Print an open message"""
        print(f"{self.name} is now open.")

