counter = 10


def wrong_function():
    counter = counter + 1
    print(counter)


try:
    wrong_function()
except UnboundLocalError as e:
    print("Error:", e)


# Correct function
def correct_function():
    global counter
    counter = counter + 1
    print("After using global:", counter)


# correct_function()
# output:
# Error: cannot access local variable 'counter' where it is not associated with a value
# After using global: 11