import re

pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'

names = ["_count2", "2fast", "total_sum"]

for name in names:
    if re.fullmatch(pattern, name):
        print(name, "-> Valid")
    else:
        print(name, "-> Invalid")
# output:
# _count2 -> Valid
# 2fast -> Invalid
# total_sum -> Valid