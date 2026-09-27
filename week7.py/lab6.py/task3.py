from functools import reduce

numbers = [2, 3, 4, 5]

# (a) Product
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)


# (b) Maximum value without max()
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)


# (c) Concatenate strings
words = ["Python", "is", "easy", "to", "learn"]

sentence = reduce(lambda a, b: a + " " + b, words)
print("Sentence:", sentence)
# output:
# Product: 120
# Maximum: 5
# Sentence: Python is easy to learn