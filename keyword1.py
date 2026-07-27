import keyword

# Get the list of Python keywords
keywords = keyword.kwlist

# Print the total number of keywords
print("Total number of keywords:", len(keywords))

# Print the full list of keywords
print("\nPython Keywords:")
for word in keywords:
    print(word)
   