# Initialize variables
still_asking = True
results = []

# Use a while loop to ask people about their dream vacation
while still_asking:
    responder = input("What's your name? ")
    dream_destination = input("Where would your dream vacation trip take you? ")
    response = {'name': responder, 'dest': dream_destination}
    results.append(response)

    # Ask whether another person would like to answer
    repeat = input("Should I ask someone else? (yes/no) ")
    if repeat.lower() == 'no':
        still_asking = False

# Print results
print("\nOkay, tabulating results...\n")
for result in results:
    print(f"{result['name'].title()} would like to go to {result['dest']}.")