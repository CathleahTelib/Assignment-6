n1= int(input("enter first number:"))
n2= int(input("enter second number:"))
n3= int(input("enter third number:"))
n4= int(input("enter fourth number:"))

print("FROM HIGHEST TO LOWEST,THE SEQUENCE IS:")

if n1>n2 and n1>n3 and n1>n4:
    print(n1)
    if n2>n3 and n2>n4:
        print(n2)
        if n3>n4:
            print(n3)
            print(n4)
        else:
            print(n4)
            print(n3)
    elif n3>n2 and n3>n4:
        print(n3)
        if n2>n4:
            print(n2)
            print(n4)
        else:
            print(n4)
            print(n2)
    else:
        print(n4)
        if n2>n3:
            print(n2)
            print(n3)
        else:
            print(n3)
            print(n2)
############################################
elif n2>n1 and n2>n3 and n3>n4:
        print(n2)
        if n1>n3 and n1>n4:
            print(n1)
            if n3>n4:
                print(n3)
                print(n4)
            else:
                print(n4)
                print(n3)
        elif n3>n1 and n3>n4:
            print(n3)
            if n1>n4:
                print(n1)
                print(n4)
            else:
                print(n4)
                print(n1)
        else:
            print(n4)
            if n1>n3:
                print(n1)
                print(n3)
            else:
                print(n3)
                print(n1)
#################################################
elif n3>n1 and n3>n2 and n3>n4:
        print(n3)
        if n1>n2 and n1>n4:
            print(n1)
            if n2>n4:
                print(n2)
                print(n4)
            else:
                print(n4)
                print(n2)
        elif n2>n1 and n2>n4:
            print(n2)
            if n1>n4:
                print(n1)
                print(n4)
            else:
                print(n4)
                print(n1)
        else:
            print(n4)
            if n1>n2:
                print(n1)
                print(n2)
            else:
                print(n2)
                print(n1)
###################################################
elif n4>n1 and n4>n2 and n4>n3:
        print(n4)
        if n1>n2 and n1>n3:
                print(n1)
                if n2>n3:
                    print(n2)
                    print(n3)
                else:
                    print(n3)
                    print(n2)
        elif n2>n1 and n2>n3:
            print(n2)
            if n1>n3:
                print(n1)
                print(n3)
            else:
                print(n3)
                print(n1)
        else:
            print(n3)
            if n1>n2:
                print(n1)
                print(n2)
            else:
                print(n2)
                print(n1)
