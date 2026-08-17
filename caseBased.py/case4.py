salary = int(input("Enter the initial salary: "))

for year in range(1, 4):
    salary += salary * 0.10
    print("Salary after year", year, "=", salary)