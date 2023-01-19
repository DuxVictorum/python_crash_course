from random import choice

# Initialize list of my favorite fruits
fave_fruits = ["banana", "apple", "kiwi", "strawberry", "mango"]
options = ["apple", "pear", "banana", "papaya", "watermelon", "grape", \
    "strawberry", "lemon", "mango", "cherry", "kiwi"]

# Use conditionals to query the contents of fave_fruits
for num in range(0,5):          # Do it 5 times
    fruit = choice(options)     # Choose a fruit
    if fruit in fave_fruits:
        print(f"You really like {fruit}s!")
    else: 
        print(f"I guess you don't like {fruit}s all that much.")
    options.remove(fruit)       # Options can only be chosen once
    