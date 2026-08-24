text = "hello"
count = {}

for x in text:
    count[x] = count.get(x, 0) + 1

print(count)