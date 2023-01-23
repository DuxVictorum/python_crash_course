# Initialize two lists
current_users = ["William", "Shirley", "ReXo", "Fahad", "Cheng Du"]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
new_users = ["Rexo", "Darlene", "Mirjat", "Thamala", "shirley"]

# Check if username is available (case-insensitive)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that username is already taken. Please choose another.")
    else: 
        print(f"The username {new_user} is available")


# TODO: Refactor to check for case