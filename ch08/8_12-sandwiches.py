# functions
def make_sandwich(*toppings):
    print("This sandwich will have:")
    for topping in toppings:
        print(f"\t- {topping}")

make_sandwich("ham", "cheese", "awesome secret sauce")
make_sandwich("marshmallows", "nutella", "whipped cherry pie filling")
make_sandwich("pickles", "peanut butter")