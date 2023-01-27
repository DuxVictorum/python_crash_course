# Make a list of dictionaries to describe three people
cool_peeps = [
    {
        'first_name': 'Charles',
        'last_name': 'Thorne',
        'age': 14,
        'city': 'Pawston'
    },
    {
        'first_name': 'Ricky',
        'last_name': 'Stillwell',
        'age': 34,
        'city': 'Louisville'
    },
    {
        'first_name': 'Robbo',
        'last_name': 'Hobbo',
        'age': 1534,
        'city': 'Arnold'
    }
]

# Print out dictionary information for all three people
count = 1
for peep in cool_peeps:
    print(f"#{count}: \t{peep['first_name']} {peep['last_name']}")
    print(f"\tAge: {peep['age']} \tCity: {peep['city']}\n")
    count += 1