list=[1,4,5,3,2]
flag =0
i=1
while i<len(list):
    if(list[i]<list[i-1]):
      flag=1
    i=i+1  
    