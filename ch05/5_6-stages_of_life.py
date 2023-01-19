# Ask user for age and convert to integer
age_input = input("How old are you? ")
age = int(age_input)

# Use conditionals to output user's "stage of life"
if age < 2:
    print("You must be a baby. Goo-goo gah-gah!")
elif age < 4:
    print("You're a toddler, growing fast.") 
elif age < 13:
    print("Hey kid. How does it feel to be your age?")
elif age < 20:
    print("So, you're a teenager now, huh? Cool.")
elif age < 65:
    print("You are considered an adult. Make decisions wisely.")
else:
    print("You are an older American. What wisdom would you like to share?")