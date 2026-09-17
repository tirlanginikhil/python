import re

text = "NASA is working with USA on a new project. The CEO visited INDIA."

matches = re.finditer(r"\b\w{7,}\b", text)

for match in matches:
    print(match.group(), "->", match.start())
# output:
# working -> 8
# project -> 34
# visited -> 51