string = input("Enter a string: ")

if string.isdigit():
    print("String contains only digits")
elif string.isalpha():
    print("String contains only alphabets")
elif string.isalnum():
    print("String is alphanumeric")
else:
    print("String contains special characters")
#     output:
#     Enter a string: nikhil
# String contains only alphabets