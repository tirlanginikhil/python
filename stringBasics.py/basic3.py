string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
# output:
# Enter a string: nikhil
# The string is not a palindrome