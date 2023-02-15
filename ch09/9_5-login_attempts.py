from random import randint

# Class to represent a system user
class User:
    """User of a campus Unix system"""

    def __init__(self, first_name, last_name, username, dept, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.dept = dept
        self.admin = admin  # boolean value
        self.login_attempts = 0
    
    def describe_user(self):
        """Print out user description"""
        print(f"Username: {self.username} -- login attempts: "
            f"{self.login_attempts}")
        print(f"Name: {self.first_name} {self.last_name} -- {self.dept}")
        if self.admin == True:
            print("\t**Admin-level user**")

    def greet_user(self):
        """Print out greeting to the user"""
        print(f"Welcome back {self.username}. Let's get to work.\n")
    
    def increment_login(self):
        """Add one to login_attempts each time the user logs in"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0

# Create empty array to hold instances of User
users = []

# Instantiate four users and add them to the array
dev_boy1 = User('Tyler', 'Rogers', 'snuffle_puffle', 'accounting')
dev_boy2 = User('Thomas', 'The Tank Engine', 'sirchuggsalot', 'finance')
tech_lead_a = User('Pratik', 'Praudhuri', 'pratik58', 'IT', True)
qa_tester5 = User('William', 'Foster', 'stardust', 'qa testing')
users.append(dev_boy1)
users.append(dev_boy2)
users.append(tech_lead_a)
users.append(qa_tester5)

# Describe the different users via a loop
for user in users:
    # Randomize number of logins
    logins = randint(1, 25)
    while logins > 0:
        user.increment_login()
        logins -= 1
    # Run methods
    user.describe_user()
    user.greet_user()

# Reset all user login attempts to 0
for user in users:
    user.reset_login_attempts()
    print(f"Resetting login attempts for user '{user.username}' "
        f"to {user.login_attempts}.")