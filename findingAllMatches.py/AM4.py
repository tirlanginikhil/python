import re

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r"\$\d+\.\d+", prices)

print("Number of prices:", len(amounts))
# output:
# Number of prices: 3