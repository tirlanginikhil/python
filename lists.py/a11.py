a = [10, 20, 30, 20]

print(a)

a.append(40)
print(a)

a.insert(1, 15)
print(a)

a.extend([50, 60])
print(a)

a.remove(20)
print(a)

a.pop()
print(a)

a.sort()
print(a)

a.reverse()
print(a)

print("Count:", a.count(20))
print("Index:", a.index(20))