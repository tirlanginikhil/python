balance = 10000
withdrawal = 4500

valid = (withdrawal <= balance) and (withdrawal % 100 == 0)

print("Withdrawal valid:", valid)