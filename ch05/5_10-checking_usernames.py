# Initialize two lists
current_users = ["William", "Shirley", "Rexo", "Fahad", "Cheng Du"]
new_users = ["Rexo", "Darlene", "Mirjat", "Thamala", "Shirley"]

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry {new_user}, that username is already taken. Please choose another.")
    else: 
        print(f"The username {new_user} is available")


# TODO: Refactor to check for case