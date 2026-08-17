READ = 4
WRITE = 2
EXECUTE = 1
permissions = READ | WRITE
has_write = bool(permissions & WRITE)

print("Permissions:", permissions)
print("Write permission set:", has_write)

