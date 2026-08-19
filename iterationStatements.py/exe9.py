num = int(input("Enter a number: "))

n = abs(num)
sum_digits = 0
count = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    count += 1
    n //= 10

average = sum_digits / count

print("Sum of digits:", sum_digits)
print("Average of digits:", average)
# output:
# Enter a number: 12
# Sum of digits: 3
# Average of digits: 1.5