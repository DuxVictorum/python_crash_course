# Initialize variables: list of pizzas and customers
from random import choice

yummy_pizzas = ["hawaiian", "pepperoni and sausage", "bbq"]
customers = ["Yondu", "Brak", "Spiderman"]

# For loop practice
for pizza in yummy_pizzas:
  print(pizza)

for pizza in yummy_pizzas:
  print(f"I've got a {pizza} pizza ready for {choice(customers)}!")

# Closing statement
print("Man, I think they really like these pizzas!")