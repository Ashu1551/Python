a = [3,1,5,4,7]
b = [2,5,8,9,0]
c = []
for i in a:
     if i in b and i in c:
       c.append([i])
print(c)