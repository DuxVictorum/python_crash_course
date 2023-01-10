# Initialize variables: 7 guests now!
dinner_guests = ["Tolkien", "Jesus", "Einstein", "Henry F. Thorne, Jr.", ]

# Dinner invitations
print(f"First up is {dinner_guests[0]}. Please come to dinner tonight at 7pm.")
print(f"Next in line is {dinner_guests[1]}, who is of course always welcome.")
print(f"Last but not least is {dinner_guests[-1]}, who is my grandfather.")
print(f"Oh darn, I forgot about {dinner_guests[2]}. He's just awesome, right?")

# Add new guests
print("\n--> Oh good, we've found a bigger table! Let's invite more people.\n")
dinner_guests.insert(0, "Buzz Lightyear")
dinner_guests.insert(3, "Bagel Shop Uncle")
dinner_guests.append("Tarzan")

# Print additional dinner announcements.
print(f"Here's a seat for {dinner_guests[0]}.")
print(f"And now one for {dinner_guests[3]}.")
print(f"And now definitely last is our new guest of honor, {dinner_guests[-1]}.\n")