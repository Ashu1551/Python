try:
    a=int(input("enter a m]number"))
    b= int(input("enter a number"))
    c=a/b
except ZeroDivisionError:
    print("devided by Zero")
except ValueError:
    print("invalide character")
else:
    print("division is",c)    