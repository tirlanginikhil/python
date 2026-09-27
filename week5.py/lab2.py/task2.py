def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price


# (a) Only price
print("Price 1:", calculate_price(1000))

# (b) Price and custom tax rate
print("Price 2:", calculate_price(1000, 10))

# (c) All arguments
print("Price 3:", calculate_price(1000, 10, 100))