def simple_interest(principal, rate, time):
    """Calculate and return simple interest."""
    si = (principal * rate * time) / 100
    return si


p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)