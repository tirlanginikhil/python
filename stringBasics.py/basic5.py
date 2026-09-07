string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in string:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
# output:
# Enter a string: nikhil
# Vowels: 2
# Consonants: 4
# Digits: 0
# Spaces: 0