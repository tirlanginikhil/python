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
# output:
# enter first number12
# enter second number13
# enter third number14
# 14 is largest
