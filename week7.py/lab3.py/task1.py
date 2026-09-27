def factorial(n):
    if n < 0:
        return "Factorial not possible for negative numbers"
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Recursive
n = int(input("Enter a number: "))
print("Factorial using recursion:", factorial(n))


# Iterative
def factorial_iterative(n):
    if n < 0:
        return "Factorial not possible"
    
    result = 1
    for i in range(1, n + 1):
        result = result * i
    
    return result


print("Factorial using iteration:", factorial_iterative(n))
# output:
# Enter a number: 5
# Factorial using recursion: 120
# Factorial using iteration: 120