
import random
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxyz"
digit="123456789"
all= capital+small+digit
length=8
password="".join(random.sample(all,length))
print("Generated password is",password)