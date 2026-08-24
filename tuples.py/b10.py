a = (10, 20, 30)

try:
    a[0] = 50
except TypeError:
    print("Tuples cannot be modified")
# output:
# Tuples cannot be modified