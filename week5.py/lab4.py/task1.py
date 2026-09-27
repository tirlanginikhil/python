# (a) Square of a number
square = lambda x: x * x

# (b) Check if a number is even
even = lambda x: x % 2 == 0

# (c) Find larger of two numbers
larger = lambda x, y: x if x > y else y


print("Square:", square(5))
print("Is Even:", even(8))
print("Larger:", larger(10, 7))