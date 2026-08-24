items = {"Pen": 10, "Bag": 500, "Book": 100, "Pencil": 5}

highest = max(items, key=items.get)
lowest = min(items, key=items.get)

print("Highest:", highest)
print("Lowest:", lowest)