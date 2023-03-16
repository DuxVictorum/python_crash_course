# Create instance of Admin separate from individual modules
from priv_admin_classes import Privileges, Admin

admin_guy = Admin('Rick', 'Ricardo', 'shakey_bacon', 'MBE', admin=True)

admin_guy.describe_user()
admin_guy.privileges.show_privileges(admin_guy.username)