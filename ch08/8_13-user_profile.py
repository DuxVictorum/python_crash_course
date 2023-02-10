# function (from p149 of book)
from distutils.command.build import build


def build_profile(first, last, **user_info):
    """Build a dictionary with user info"""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

# Call function
user_profile1 = build_profile(
    'William', 'Thorne', color='yellow', number=11, age=5
)
print(user_profile1)