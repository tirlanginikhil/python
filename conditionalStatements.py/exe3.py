x=int(input("enter first side"))
y=int(input("enter second side"))
z=int(input("enter third side"))
if x==y and y==z:
    print("equilateral")
elif x==y or y==z or z==x:
    print("isosceles")
else:
    print("scalene")
# output:
# enter first side12
# enter second side12
# enter third side13
# isosceles