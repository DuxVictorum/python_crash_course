# Initialize a list of sandwiches -- lots of pastrami -- and an empty list
sandwich_orders = ['honky tonk', 'pastrami', 'regis philly', 
'salami joe', 'pastrami', "pike's peak", 'pastrami']
finished_sandwiches = []

# Uh-oh, out of pastrami!
print("Welcome to Al's Deli. We are out of pastrami today.")

# Run while loop to process through the orders
while sandwich_orders:
    order = sandwich_orders.pop(0)
    if order != 'pastrami':
        print(f"Making a {order} sandwich...")
        finished_sandwiches.append(order)

# Summarize orders made
print(f"* * * *\nI just made the following {str(len(finished_sandwiches))} "
        "sandwiches: ")
for s in finished_sandwiches:
    print(f'\t{s}')
