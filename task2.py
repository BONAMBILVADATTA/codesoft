import sys
def maths(c):
    if c==1:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        print(a+b)
    elif c==2:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        print(a-b)
    elif c==3:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        print(a*b)
    elif c==4:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        print(a/b)
    elif c==5:
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        print(a%b)
    elif c==6:
        sys.exit(1)
    else:
        sys.exit(1)
while True:
    print("select option")
    print("1.addition")
    print("2.subtraction")
    print("3.multipication")
    print("4.division")
    print("5.modulus")
    print("6.exit")
    c=float(input("enter the choice:"))
    maths(c)

   
