import re

sentence = "1024 requests were served in 3 seconds"

result = re.search(r"served", sentence)

if result:
    print("Word found")
    print("Start and end position:", result.span())
else:
    print("Word not found")
# output:
# Word found
# Start and end position: (19, 25)