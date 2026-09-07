string = input("Enter a string: ")
character = input("Enter the character to count: ")

count = 0

for char in string:
    if char == character:
        count += 1

print("Occurrences:", count)
#output:
# Enter a string: nikhil
# Enter the character to count: i
# Occurrences: 2