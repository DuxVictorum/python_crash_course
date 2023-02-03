# Initialize a list of sandwiches and an empty list
sandwich_orders = ['honky tonk', 'regis philly', 'salami joe', "pike's peak"]
finished_sandwiches = []

# Run while loop to process through the orders
while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"Making a {order} sandwich...")
    finished_sandwiches.append(order)

# Summarize orders made
print(f"* * * *\nI just made the following {str(len(finished_sandwiches))} "
        "sandwiches: ")
for s in finished_sandwiches:
    print(f'\t{s}')
