percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 75
print("Eligible for scholarship:", eligible)
#output:
# Enter percentage: 78
# Enter attendance %: 78
# Eligible for scholarship: True
