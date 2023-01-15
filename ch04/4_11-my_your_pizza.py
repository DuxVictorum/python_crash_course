from random import choice

# Initialize variables: list of pizzas and customers
my_pizzas = ["hawaiian", "pepperoni and sausage", "bbq"]
your_pizzas = my_pizzas[:]
customers = ["Yondu", "Brak", "Spiderman"]

# Add a unique item to each pizza list
my_pizzas.append("olive and mushroom")
your_pizzas.append("pizzarito")

# Prove that each list is unique and not one pointing to another
for pizza in my_pizzas:
  print(f"I've got a {pizza} pizza from me ready for {choice(customers)}!")

print('')

for pizza in your_pizzas:
  print(f"I've got a yummy {pizza} pizza from you ready for {choice(customers)}.")
# Closing statement
print("Man, I think everyone really likes their pizzas!")