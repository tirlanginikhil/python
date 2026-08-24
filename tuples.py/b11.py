a = (10, [20, 30], 40)

a[1].append(50)

# The tuple is immutable, but the nested list is mutable.
# So, the contents of the list can be changed.

print(a)