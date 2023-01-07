# Adding comments this time

# Program re-factor #1
# Variable assignment
name1 = "\nRubble\t"
name2 = "\n\tMarshall"
name3 = "\t\tWilliam's dad\n\n"
# Print commands, practicing use of strip string methods
print(name1, name2)
print(name1.rstrip(), name2.lstrip(), name3.strip())

# Program re-factor #2
# Variable assignment
famous_quotation = '"We\'re gonna need guns. Lots of guns."'
source = "Keanu Reeves"
role = "Neo"
film = "The Matrix"
# Practice with f-strings
print(f'{source}, playing {role} in the film {film}, is famous for saying {famous_quotation}')