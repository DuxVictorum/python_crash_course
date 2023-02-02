# Ask user in a loop for toppings until they type 'quit'
toppings = []

while True:
    topping = input("Add a topping to your pizza. ('quit' to stop) ")
    # Exit 1
    if topping.lower() == 'quit': 
        break
    print(f"Adding {topping} to your pizza...")
    toppings.append(topping)
    # Exit 2
    if len(toppings) == 3:
        print("That's three toppings.")
        break

# Ask user in a loop for soda or lemonade (other input causes loop to repeat)
drink = ''
needs_drink = True
while needs_drink:
    drink = input("Soda or lemonade for your drink? ")
    if drink.lower() == 'soda' or drink.lower() == 'lemonade':
        print(f"Good choice, {drink} is always yummy with pizza.")
        needs_drink = False
    else:
        print("Let's try that again...")

print(f"\nYou've ordered a {drink} and pizza with the following toppings:")
for t in toppings:
    print(f'\t{t}')