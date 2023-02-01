# Ask user in a loop for toppings until they type 'quit'
toppings = []
while True:
    topping = input("Add a topping to your pizza?  ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)

print(toppings)