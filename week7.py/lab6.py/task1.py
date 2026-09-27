# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


temperatures = [0, 10, 20, 30, 40]

fahrenheit = list(map(celsius_to_fahrenheit, temperatures))

print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)


# Convert strings to uppercase
def to_uppercase(s):
    return s.upper()


words = ["python", "java", "c", "javascript"]

uppercase_words = list(map(to_uppercase, words))

print("Original:", words)
print("Uppercase:", uppercase_words)
# output:
# Celsius: [0, 10, 20, 30, 40]
# Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]
# Original: ['python', 'java', 'c', 'javascript']
# Uppercase: ['PYTHON', 'JAVA', 'C', 'JAVASCRIPT']