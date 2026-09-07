s1 = input("Enter a string: ")
c = input("Enter a character: ")

first = s1.find(c)
last = s1.rfind(c)

print("First occurrence index:", first)
print("Last occurrence index:", last)
# output:
# Enter a string: nikhil
# Enter a character: i
# First occurrence index: 1
# Last occurrence index: 4