import re

text = "My exams are on 15/06/2024 and 25/07/2024."

pattern = r'(\d{2})/(\d{2})/(\d{4})'

dates = re.findall(pattern, text)

print("Dates:", dates)

result = re.sub(pattern, r'\3-\2-\1', text)

print("Reformatted:", result)
# output:
# Dates: [('15', '06', '2024'), ('25', '07', '2024')]
# Reformatted: My exams are on 2024-06-15 and 2024-07-25.