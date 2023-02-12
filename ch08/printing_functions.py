# Module for holding functions related to 8_15-printing_models.py

# Functions
def print_models(unprinted_designs, completed_models):
    """Simulate the printing of designs followed by showing completed status"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all printed models"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(f"\t- {completed_model}")