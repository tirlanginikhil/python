a = [10, -5, 20, -3, 7]

b = [0 if x < 0 else x for x in a]
print(b)
# output:
# [10, 0, 20, 0, 7]