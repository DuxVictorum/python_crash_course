# Initialize dictionary of people and their favorite places
fave_places = {
    'Snuffle': ['bedroom', 'kitchen', 'California'],
    'Buffy': ['bedroom', 'game board', 'St. Louis', 'Washington, DC'],
    'Puppy': ['living room', 'car', 'New York City']
}

# Loop the dictionary and print out results
print("Let's see our guests' favorite places!")
for k, v in fave_places.items():
    print(f"{k} likes being in:")
    for place in v:
        if place[0].isupper():
            print(f"\t{place}")
        else:
            print(f"\ta {place}")