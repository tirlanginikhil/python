s = input("Enter a string: ")
old = input("Enter the character/word to replace: ")
new = input("Enter the new character/word: ")
result=""
for i in s:
    if i==old:
        result+=new
    else:
        result+=i


print("After replacement:", result)
# output:
# Enter a string: nikhil
# Enter the character/word to replace: k
# Enter the new character/word: h
# After replacement: nihhil