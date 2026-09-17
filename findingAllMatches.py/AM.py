import re

text = "NASA is working with USA on a new project. The CEO visited INDIA."

words = re.findall(r"\b[A-Z]{2,}\b", text)

print(words)
# output:
# ['NASA', 'USA', 'CEO', 'INDIA']