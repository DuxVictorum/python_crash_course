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
print(f"Please come, {dinner_guests[0]}.")
print(f"We've made a special dish just for you, {dinner_guests[3]}, so please come.")
print(f"And a special appeal to our guest of honor, {dinner_guests[-1]}!\n")

# Shrink the invite list
print("Oooooh shoot. I forgot. We only have enough food for two people.")
dinner_guests.pop(-1)
dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()
for guest in dinner_guests:
  print(f"You are still welcome to come, {guest}. We've made deliciou sushi!")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)