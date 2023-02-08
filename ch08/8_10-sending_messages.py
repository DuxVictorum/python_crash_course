# Functions
def send_messages(msgs):
    """Print out a list of messages passed in and 'send' them"""
    msg_num = 1
    print(f"Printing out {len(msgs)} messages:")
    while msgs:
        msg = msgs.pop(0)
        print(f"\t#{msg_num} - {msg}")
        msg_num += 1
        sent_messages.append(msg)

# Create sample list of messages and an empty 'sent' list
messages = [
    'Hello, Rashid!', 
    'Where did you park?',
    'You parked all the way over there!',
    'You know how much they charge there, right?',
    'Get over here now, bro.'
    ]
sent_messages = []

# Call the function by passing in a *copy* of the list
send_messages(messages)

# Verify thatmessages is empty and sent_messages is populated
print(messages)
print(sent_messages)