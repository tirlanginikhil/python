def build_profile(**details):
    print("----- PROFILE -----")

    for key, value in details.items():
        print(key, ":", value)

    print("-------------------")


# First profile
build_profile(name="Nikhil", age=18, city="Srikakulam", hobby="Movies")

print()

# Second profile
build_profile(name="Ravi", age=19, city="Vizag", hobby="Cricket")
# output:
# ----- PROFILE -----
# name : Nikhil
# age : 18
# city : Srikakulam
# hobby : Movies
# -------------------

# ----- PROFILE -----
# name : Ravi
# age : 19
# city : Vizag
# hobby : Cricket
# -------------------