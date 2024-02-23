a=[1,2,5,4,7]
b=[2,5,8,9,0]
c=[]
for i in a:
    if i in b and i not in c:
       c.append([i])
print(c)