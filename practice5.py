#leep year or not
year=eval(input("Enter the year="))
if(year%4==0 and year%100!=0)or(year%400==0):
    print("it is a leap year",year)
else:
    print("it is not leap year",year )
    