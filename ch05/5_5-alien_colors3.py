from random import choice

# Initialize alien color
colors = ["green", "yellow", "red"]
alien_color = choice(colors)
points = 0

# Practicing if statements
if alien_color == "green":
    points += 5
    print(f"You got a green one! You've earned {points} points.")
elif alien_color == "yellow":
    points += 10
    print(f"Awesome, a yellow alien goes down. That's 10 more points.")
else:
    points += 15
    print(f"Wow, you nailed a red one for another 15 points for {points} points total!")
