# Initialize list of usernames
usernames = []

if usernames:   # Check for empty usernames list
    # Practice conditionals with lists
    for user in usernames:
        if user == "admin":
            print("Welcome back, database admin. Please check for system updates.")
        else: 
            print(f"User {user}, you are now logged into the system.")
else:
    print("Alas, there are no usernames to check.")