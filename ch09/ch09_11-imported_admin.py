# Practice importing classes
from admin_classes import Admin

# Make instance of class
admin_23 = Admin('Snuffle', 'Bear', 'snufflepuffle', 'IT')

# Call methods
admin_23.describe_user()
admin_23.greet_user()
admin_23.privileges.show_privileges(admin_23.username)