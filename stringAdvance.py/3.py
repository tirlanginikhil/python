string = input("Enter a string: ")

for ch in string:
    if string.count(ch) > 1:
        print(ch, ":", string.count(ch))
# output:
# Enter a string: nikhil
# i : 2
# i : 2