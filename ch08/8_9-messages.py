# Functions
def show_messages(msgs):
    """Print out a list of messages passed in"""
    msg_num = 1
    print(f"Printing out {len(msgs)} messages:")
    for msg in msgs:
        print(f"\t#{msg_num} - {msg}")
        msg_num += 1

# Create sample list of messages
messages = [
    'Hello, Fred!', 
    'When are you coming with the chicken?',
    'Are you still there? Seriously?',
    'I need me some hot, delicious chicken right now!'
    ]

# Call the function
show_messages(messages)