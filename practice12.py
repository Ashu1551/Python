#fuction program addition
def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
# to call the function
z1,z2,z3=add(10,20)
print("Addition is =",z1)
print("subtraction is =",z2)
print("multiplication is =",z3)
# to call the function
x=eval(input("enter the first no. ="))
y=eval(input("enter the second no. ="))
z=add(x,y)
print("Addition is =",z[0])
print("subtraction is =",z[1])
print("multiplication is =",z[2])
