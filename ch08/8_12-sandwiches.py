# functions
def make_sandwich(*toppings):
    """Take in tuple (of arbitrary length) of toppings, then print them"""
    print("This sandwich will have:")
    for topping in toppings:
        print(f"\t- {topping}")

# Call function three times
make_sandwich("ham", "cheese", "awesome secret sauce")
make_sandwich("marshmallows", "nutella", "whipped cherry pie filling")
make_sandwich("pickles", "peanut butter")