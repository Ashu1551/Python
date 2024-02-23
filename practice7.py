#division program
text=input("math  physics and chemistry")
m,p,c=text.split()
total=int(m)+int(p)+int(c) 
print("total marks",total)
per=total/3
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