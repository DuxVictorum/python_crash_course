# Initialize dictionary of programming terms
coding_terms = {
    'string': 'sequence of characters used to represent text',
    'number': 'numerical characters used to represent numbers',
    'list': 'a set of comma-separated values',
    'conditional': 'statement that will execute only if '
        'the condition evaluates to true',
    'method': 'function that belongs to an object type'
}

# Print out all the terms and definitions
print("Let's review some important coding terms we've learned:")
for k, v in coding_terms.items():
    if k == 'conditional':
        print(f"\t{k}:\t{v}")
    else:
        print(f"\t{k}:\t\t{v}")