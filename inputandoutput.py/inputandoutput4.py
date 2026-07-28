# Taking multiple values in a single line
numbers = input("Enter numbers separated by spaces: ")

# Splitting the input and converting each value to an integer
num_list = list(map(int, numbers.split()))

# Calculating and printing the sum
print("Sum =", sum(num_list))