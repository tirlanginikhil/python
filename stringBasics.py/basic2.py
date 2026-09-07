string = input("Enter a string: ")

reverse = ""

for char in string:
    reverse = char + reverse

print("Reversed string:", reverse)
# output:
# Enter a string: nihil
# Reversed string: lihin