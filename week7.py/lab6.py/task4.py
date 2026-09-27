from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter even numbers
evens = filter(lambda x: x % 2 == 0, nums)

# Step 2: Square the even numbers
squares = map(lambda x: x ** 2, evens)

# Step 3: Find total
total = reduce(lambda a, b: a + b, squares)

print("Total:", total)
# output:
# Total: 220