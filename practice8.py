#insurance provide or not
ms=input("Enter the marital status=")
gender=input("Enter the gender=")
age=int(input("Enter the age="))
if(ms=='M'):
    print("insurance is provide")
elif(gender=='m'):
    if(age>40):
        print("insurance is provide")
    else:
        print("insurance is not provide")
elif(age>35):
    print("insurance is provide")
else:
    print("insurance is not provide")
