# Initialize list of usernames
usernames = ["fr27", "alice", "sharhen", "rheinhorst", "admin"]

# Practice conditionals with lists
for user in usernames:
    if user == "admin":
        print("Welcome back, database admin. Please check for system updates.")
    else: 
        print(f"User {user}, you are now logged into the system.")