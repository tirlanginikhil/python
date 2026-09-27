def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


# Positional arguments
student_info("Nikhil", "25341A05L4", "CSE")

print()

# Keyword arguments in different order
student_info(branch="CSE", name="Nikhil", roll_no="25341A05L4")
# output:
# Name: Nikhil
# Roll No: 25341A05L4
# Branch: CSE

# Name: Nikhil
# Roll No: 25341A05L4
# Branch: CSE