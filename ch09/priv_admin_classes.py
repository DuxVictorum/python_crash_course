from user_class import User

# Module for Privileges class
class Privileges:
    """Represents user privileges"""
    def __init__(self):
        self.privileges = [
            'can add user',
            'can modify user',
            'can change group ownership levels', 
            'can send anonymous messages',
            'can get sushi delivered direct to his door'
        ]
    
    # Method for displaying admin privileges
    def show_privileges(self, username):
        """Display list of privileges"""
        print(f"Admin user '{username}' possesses the following "
            f"privileges:")
        for p in self.privileges:
            print(f"  - {p}")


# Class for admin user
class Admin(User):
    """Represent an admin-level user"""
    def __init__(self, first_name, last_name, username, dept, admin=True):
        super().__init__(first_name, last_name, username, dept, admin)

        self.privileges = Privileges()