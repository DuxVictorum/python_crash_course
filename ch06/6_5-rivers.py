# Initialize dictionary of rivers and their associated state
rivers = {
    'Meramec': 'Missouri',
    'Upper Iowa': 'Iowa',
    'Hudson': 'New York'
}

# Loop through the k-v pairs, then the keys, and finally the values
for k, v in rivers.items():
    print(f"The {k} River flows in the state of {v}.")

print("Here are the rivers:")
for river in rivers:
    print(f'\t{river}')

print("Here are the states:")
for state in rivers.values():
    print(f'\t{state}')