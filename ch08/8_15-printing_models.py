import printing_functions as pf

# Initialize lists
unprinted_designs = ['phone case', 'robot laser gun', 'triskaidecahedron']
completed_models = []

# Call imported functions
pf.print_models(unprinted_designs, completed_models)

pf.show_completed_models(completed_models)