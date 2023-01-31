# Ask the number of people in the dinner group
num_diners = input("How people in your party tonight?  ")

# Check to see if the party will need to wait or not
if int(num_diners) > 8:
    print(f"I'm sorry, {num_diners} is too large to seat right now. "
    "You'll have to wait.")
else:
    print("Great, you can come with me to your table now!")