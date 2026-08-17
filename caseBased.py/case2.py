first_name = input("Enter your first name: ")
roll_number = input("Enter your roll number: ")

username = first_name.lower() + roll_number[-2:]

print("Username:", username)