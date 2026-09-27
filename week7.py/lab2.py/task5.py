def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)

    print("Ordered Items:")
    for item in items:
        print("-", item)

    print("Discount:", discount)

    print("Extra Information:")
    for key, value in extra.items():
        print(key, ":", value)


order_summary(
    "Nikhil",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=500,
    delivery_address="Srikakulam",
    gift_wrap="Yes"
)
# output:
# Customer: Nikhil
# Ordered Items:
# - Laptop
# - Mouse
# - Keyboard
# Discount: 500
# Extra Information:
# delivery_address : Srikakulam
# gift_wrap : Yes