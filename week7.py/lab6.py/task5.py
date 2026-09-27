from functools import reduce

employees = [
    {"name": "Ravi", "department": "CSE", "salary": 30000},
    {"name": "Sita", "department": "ECE", "salary": 28000},
    {"name": "Amit", "department": "CSE", "salary": 35000},
    {"name": "Priya", "department": "CSE", "salary": 32000},
    {"name": "Rahul", "department": "ECE", "salary": 30000}
]

# Select employees from CSE department
cse_employees = filter(
    lambda emp: emp["department"] == "CSE",
    employees
)

# Give selected employees a 10% salary hike
hiked_employees = list(
    map(
        lambda emp: {
            "name": emp["name"],
            "department": emp["department"],
            "salary": emp["salary"] * 1.10
        },
        cse_employees
    )
)

# Calculate total salary
total_salary = reduce(
    lambda a, b: a + b["salary"],
    hiked_employees,
    0
)

print("Employees after 10% hike:")

for emp in hiked_employees:
    print(emp)

print("Total salary expenditure:", total_salary)
# output:
# Employees after 10% hike:
# {'name': 'Ravi', 'department': 'CSE', 'salary': 33000.0}
# {'name': 'Amit', 'department': 'CSE', 'salary': 38500.00000000001}
# {'name': 'Priya', 'department': 'CSE', 'salary': 35200.00000000001}
# Total salary expenditure: 106700.00000000001