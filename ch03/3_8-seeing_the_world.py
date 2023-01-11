# Initialize variables; list of places to go
places_to_go = ["Newcastle", "Bali", "Namibia", "Olympia National Park", "Aosta"]
print(places_to_go)

# Practice with temporary sorting and reversing
print(sorted(places_to_go))
print(places_to_go)
print(sorted(places_to_go, reverse=True))
print("The order of items has still not changed!", places_to_go)

# Reversing the list permanently
places_to_go.reverse()
print("\n...But now it has.", places_to_go)
places_to_go.reverse()
print("And now it's back again with another reverse.", places_to_go)

# Sorting the list permanently (and alphabetically)
places_to_go.sort()
print("Now the list is sorted alphabetically, for good.", places_to_go)
places_to_go.sort(reverse=True)
print("And once again it's been reversed, for good.", places_to_go)


