import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@timer
def calculate_sum():
    total = 0

    for i in range(1000000):
        total = total + i

    return total


print("Sum:", calculate_sum())
# output:
# Execution time: 0.045 seconds
# Sum: 499999500000