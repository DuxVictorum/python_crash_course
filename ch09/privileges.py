# Class used with Ex. 9-8
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