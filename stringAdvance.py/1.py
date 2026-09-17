string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result = result + ch

print("After removing duplicates:", result)
# output:
# Enter a string: nikhil
# After removing duplicates: nikhl