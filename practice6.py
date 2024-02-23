#division program
m=eval(input("enter the first subject number"))
p=eval(input("enter the second subject number"))
c=eval(input("enter the third subject number"))
total=m+p+c 
print("total marks",total)
per=total/3.0
print("percentage",per)
if(per>=75):
    print("Excellent")
elif(per>=60):
    print("First division")
elif(per>=50):
    print("Second division")
elif(per>=40):
    print("third division")
else:
    print("fail")