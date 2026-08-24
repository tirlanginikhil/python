student = {"name": "Rahul", "age": 18, "mark": 85}

student.pop("age")
print(student)

x = student.get("phone", "Key not found")
print(x)