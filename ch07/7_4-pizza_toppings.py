# Ask user in a loop for toppings until they type 'quit'
toppings = []
while True:
    topping = input("Add a topping to your pizza?  ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza...")
    toppings.append(topping)

print(f"\nYou've ordered a pizza with the following toppings:")
for t in toppings:
    print(f'\t{t}')