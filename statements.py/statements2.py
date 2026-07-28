# Using the line continuation character (\)
total1 = 10 + 20 + 30 + \
         40 + 50 + 60

print("Total using line continuation:", total1)

# Using implicit continuation with parentheses ()
total2 = (
    10 + 20 + 30 +
    40 + 50 + 60
)

print("Total using parentheses:", total2)