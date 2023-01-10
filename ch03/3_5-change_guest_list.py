# Initialize variables
dinner_guests = ["Tolkien", "Jesus", "Einstein", "Henry F. Thorne, Jr."]

# Changing the guest list
no_invite = dinner_guests.pop(2)
new_invite = "Macho Man Randy Savage"
dinner_guests.append(new_invite)

# Dinner invitations
print(f"First up is {dinner_guests[0]}. Please come to dinner tonight at 7pm.")
print(f"Next in line is {dinner_guests[1]}, who is of course always welcome.")
print(f"At this point I was going to announce {no_invite}, but he can't make it anymore.")
print(f"Last but not least is {dinner_guests[2]}, who is my grandfather.")
print(f"Oh darn, I forgot about {dinner_guests[-1]}. He's just awesome, right?")

