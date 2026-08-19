x=int(input("enter first side"))
y=int(input("enter second side"))
z=int(input("enter third side"))
if x==y and y==z:
    print("equilateral")
elif x==y or y==z or z==x:
    print("isosceles")
else:
    print("scalene")