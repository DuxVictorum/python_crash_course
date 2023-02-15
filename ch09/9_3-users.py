# Class to represent a system user
class User:
    """User of a campus Unix system"""

    def __init__(self, first_name, last_name, username, dept, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.dept = dept
        self.admin = admin  # boolean value
    
    def describe_user(self):
        print(f"Username: {self.username}")
        print(f"Name: {self.first_name} {self.last_name} -- {self.dept}")
        if self.admin == True:
            print("\t**Admin-level user**")

    def greet_user(self):
        print(f"Welcome back {self.username}. Let's get to work.\n")

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

# Call methods on the different users via a loop
for user in users:
    user.describe_user()
    user.greet_user()