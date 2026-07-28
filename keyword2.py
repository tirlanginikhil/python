import keyword

# Take input from the user
word = input("Enter a word: ")

# Check if it is a Python keyword
if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is not a Python keyword.")
    #output
    Enter a word: else
else is a Python keyword.
