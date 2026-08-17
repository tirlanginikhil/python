color = input("Enter signal color: ")

valid_colors = ["red", "yellow", "green"]

if color.lower() in valid_colors:
    print("Valid traffic light color")
else:
    print("Invalid traffic light color")