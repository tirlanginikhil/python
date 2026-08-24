text = "hello"
count = {}

for x in text:
    count[x] = count.get(x, 0) + 1

print(count)
# output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}