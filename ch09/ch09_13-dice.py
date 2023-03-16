from random import randint

# Class to represent a die
class Die:
    """Represents a die for use in a game"""
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)


# Instance of die
d6 = Die(6)

# Roll the dice!
total = 0
print("Now rolling 5 times...")
for i in range(1,6):
    roll = d6.roll_die()
    print(roll)
    total += roll

print(f"The total from the dice rolls is: {total}")