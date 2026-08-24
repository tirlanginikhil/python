a = {10, 20, 30, 40}

a.remove(20)
print(a)

a.discard(50)
print(a)

# remove() gives an error if the element does not exist.
# discard() does not give an error if the element does not exist.