#function for simple interest
def si(p,r,t):
    c=p*r*t/100
    return c
#to call function   
z=si(10.00,20.00,12.00)
print("Simple interest",z)
#to call function
i=eval(input("Enter the principle"))
j=eval(input("Enter the rate"))
k=eval(input("Enter the time"))
z=(i,j,k)
print("Simple interest is=",z)