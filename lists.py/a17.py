words = ["apple", "cat", "banana", "dog", "mango"]

a = [x for x in words if len(x) > 4]
print(a)
# output:
# ['apple', 'banana', 'mango']