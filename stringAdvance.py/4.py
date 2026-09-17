string = input("Enter a string: ")

characters = list(string)
print("List:", characters)

new_string = "".join(characters)
print("String:", new_string)
# output:
# Enter a string: nikhil
# List: ['n', 'i', 'k', 'h', 'i', 'l']
# String: nikhil