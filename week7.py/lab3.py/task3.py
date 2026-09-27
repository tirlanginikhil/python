def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def reverse_number(n):
    if n < 10:
        return n

    digits = len(str(n))
    return (n % 10) * (10 ** (digits - 1)) + reverse_number(n // 10)


n = int(input("Enter a positive number: "))

print("Sum of digits:", sum_of_digits(n))
print("Reversed number:", reverse_number(n))
# output:
# Enter a positive number: 12
# Sum of digits: 3
# Reversed number: 21