# Define a function for describing a t-shirt
def make_shirt(text, size='large'):
    """Take in arguments to create a t-shirt (default size is 'large')"""
    print(f"You have ordered a size {size} t-shirt that reads {text}.")

# Call the function
make_shirt("\"What's up, homie?\"", 'small')
make_shirt("\"What an honor to serve ice cream\"")