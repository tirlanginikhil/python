x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
if x>y:
    if x>z:
        print(x,"is largeast")
    else:
        print(z,"is largest")
else:
    if y<z:
        print(z,"is largest")
    else :
        print(y,"is largest")
