student = {"name": "Rahul", "age": 18, "mark": 85}

print("Keys:")
for x in student.keys():
    print(x)

print("Values:")
for x in student.values():
    print(x)

print("Key-Value pairs:")
for x, y in student.items():
    print(x, y)
# output:
# Keys:
# name
# age
# mark
# Values:
# Rahul
# 18
# 85
# Key-Value pairs:
# name Rahul
# age 18
# mark 85