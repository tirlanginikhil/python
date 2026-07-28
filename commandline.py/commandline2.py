# sum.py

import sys

# Check if exactly two numbers are passed
if len(sys.argv) != 3:
    print("Usage: python sum.py <number1> <number2>")
else:
    # Convert command line arguments to integers
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Calculate and print the sum
    print("Sum =", num1 + num2)