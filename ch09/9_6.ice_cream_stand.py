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
        print(f"{self.name} is now open.")


# Child Class
class IceCreamStand(Restaurant):
    """Child class to represent an ice cream stand"""
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['cherry', 'vanilla', 'mentos', 'honey almond', 
            'pineapple']
    
    def show_flavors(self):
        """List out all the available flavors"""
        print("Here are the ice cream flavors today: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Make an instance and call some methods
stand_1 = IceCreamStand("O'Blaney's", "milkshakes and")
stand_1.describe_restaurant()
stand_1.open_restaurant()
stand_1.show_flavors()