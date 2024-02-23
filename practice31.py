def myname(name):
   
    l=name.split()
    new=""
    for i in range(len(l)-1):
        name=l[i]
        new=new+(l[0].upper)
    return new

    

          
 
name = input("Enter your full name")
print(myname(name))
