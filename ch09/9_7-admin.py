# Class to represent a system user (reusing 9_5-login_attempts.py)
from cgi import print_environ


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

# Class for admin user
class Admin(User):
    """Represent an admin-level user"""
    def __init__(self, first_name, last_name, username, dept, admin=True):
        super().__init__(first_name, last_name, username, dept, admin)
        # Attribute only for admins
        self.privileges = [
            'can add user',
            'can modify user',
            'can change group ownership levels', 
            'can get sushi delivered direct to his door'
            ]
    
    # Method for displaying admin privileges
    def show_privileges(self):
        """Display list of privileges"""
        print(f"Admin user '{self.username}' possesses the following "
            f"privileges:")
        for p in self.privileges:
            print(f"  - {p}")


# Make instance of class
admin_1 = Admin('Mondo', 'Diaz', 'woz', 'BSF')

# Call method
admin_1.show_privileges()