from math import factorial
from re import I


#factorial program
n=int(input("Enter a number="))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print("the factorial is",fact)