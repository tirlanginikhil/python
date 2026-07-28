# Initial values
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# (a) Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping using a temporary variable:")
print("a =", a)
print("b =", b)

# Reset values
a = 10
b = 20

# (b) Swapping using tuple unpacking
a, b = b, a

print("\nAfter swapping using tuple unpacking:")
print("a =", a)
print("b =", b)