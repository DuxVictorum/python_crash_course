# Functions
def send_messages(msgs):
    """Print out a list of messages passed in and 'send' them"""
    msg_num = 1
    print(f"Printing out {len(msgs)} messages:")
    for msg in msgs:
        print(f"\t#{msg_num} - {msg}")
        msg_num += 1
        sent_messages.append(msg)

# Create sample list of messages and an empty 'sent' list
messages = [
    'What should we watch tonight?', 
    'I dunno, maybe a musical?',
    "Oooh, right, let's watch 'Murder At Midnight'",
    'A movie with a title like that is a musical?',
    "Oh sure, it's a mystery murder musical of mayhem! 3 stars."
    ]
sent_messages = []

# Call the function by passing in a *copy* of the list
send_messages(messages[:])

# Verify that sent_messages was populated
print(messages)
print(sent_messages)