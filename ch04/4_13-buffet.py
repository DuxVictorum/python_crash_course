# Initialize tuple with 5 buffet items
buffet_items = ("chicken", "rice", "mac and cheese", "pie", "corn on the cob")

# Print out initial list
print("Our original buffet lineup consisted of: ")
for item in buffet_items:
  print("\t", item)

# Rebuild the tuple by re-assigning it a modified set of values
buffet_items = ("chicken", "green beans", "pie", "peach cobbler", "fried yams")
print("Our new lineup consists of: ")
for item in buffet_items:
  print(f"\t{item}", end=' ')