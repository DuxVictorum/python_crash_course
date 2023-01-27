# Initialize a dictionary of people and their favorite coding language
fave_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# List of people who I want in the above dictionary
cool_coders = ['alice', 'edward', 'william', 'terrence', 'jen']

# Use a loop to check if each coder has indicated their favorite language
for coder in cool_coders:
    if coder in fave_languages.keys():
        print(f"Thanks, {coder.title()}, you have chosen "
        "{fave_languages[coder]}.")
    else:
        print(f"{coder.title()}, you haven't told us yet which language is "
        "your favorite.")