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
        print(f"Name: {self.first_name} {self.last_name} -- {self.dept} dept")
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
