import re

sentence = "I have a cat and a dog. My friend has a bird."

pattern = r'\b(cat|dog|bird)\b'

pets = re.findall(pattern, sentence)

print(pets)
# output:
# ['cat', 'dog', 'bird']