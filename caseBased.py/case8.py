percentage=int(input("Enter percentage: "))
income=int(input("Enter income: "))
valid=(percentage>85)or((percentage>=75)and(income<200000))
print("valid",valid)