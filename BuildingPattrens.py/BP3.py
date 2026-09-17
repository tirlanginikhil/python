import re

pattern = r'#[A-Fa-f0-9]{3}([A-Fa-f0-9]{3})?'

colors = ["#FFAA00", "#000", "#12AB", "#GGG"]

for color in colors:
    if re.fullmatch(pattern, color):
        print(color, "-> Valid")
    else:
        print(color, "-> Invalid")
# output:
# #FFAA00 -> Valid
# #000 -> Valid
# #12AB -> Invalid
# #GGG -> Invalid