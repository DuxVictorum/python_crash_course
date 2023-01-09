authors = ["Shakespeare", "Proust", "Tolstoy", "Barton"]
print(authors)
authors.append("Smartypants")

for a in authors:
  print(f"You should read {a}.")

del authors[2]
print(authors)