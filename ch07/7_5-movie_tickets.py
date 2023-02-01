# Ask user for their age
while True:
    age = input("Welcome to Crown Theatres. How old are you?  ")
    if age.lower() == 'quit':
        print("Alright, we'll see you later!")
        break
    age = int(age)

    # Use conditionals to calculate the ticket price
    if age > 12:
        print("Your ticket will be $15.")
    elif age > 2:
        print("Your ticket will be $10")
    else:
        print("Your ticket is free.")