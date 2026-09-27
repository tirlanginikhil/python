import time


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start, "seconds")

        return result

    return wrapper


@log_call
@timer
def add(a, b):
    return a + b


print("Result:", add(10, 20))
# output:
# Calling add
# Execution time: 0.000001 seconds
# add returned 30
# Result: 30