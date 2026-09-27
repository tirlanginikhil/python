from functools import wraps

is_logged_in = True


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login first.")

    return wrapper


@require_login
def view_profile():
    print("Welcome to your profile.")


# When logged in
is_logged_in = True
view_profile()


# When not logged in
is_logged_in = False
view_profile()
# output:
# Welcome to your profile.
# Access denied. Please login first.