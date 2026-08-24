a = [10, 25, 5, 40, 15]

maximum = a[0]
minimum = a[0]
total = 0

for x in a:
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
    total = total + x

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)