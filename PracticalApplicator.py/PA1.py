import re

def is_valid_email(s):
    pattern = r'^[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'
    return bool(re.fullmatch(pattern, s))

valid = [
    "john@gmail.com",
    "abc.xyz@yahoo.in",
    "student123@college.edu",
    "a.b@example.co"
]

invalid = [
    "a@b.c",
    "no-at-sign.com",
    "@gmail.com",
    "abc@gmail"
]

for email in valid:
    print(email, "->", is_valid_email(email))

for email in invalid:
    print(email, "->", is_valid_email(email))
#     output:
#     john@gmail.com -> True
# abc.xyz@yahoo.in -> True
# student123@college.edu -> True
# a.b@example.co -> True
# a@b.c -> False
# no-at-sign.com -> False
# @gmail.com -> False
# abc@gmail -> False