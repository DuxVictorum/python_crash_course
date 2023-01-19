from random import choice

# Initialize alien color
colors = ["green", "yellow", "red"]
alien_color = choice(colors)
points = 0

# Practicing if statements
if alien_color == "green":
    points += 5
    print(f"You got a green one! You've earned {points} points.")
else:
    points += 10
    print(f"Wow, that's another 10 points for {points} points total!")
