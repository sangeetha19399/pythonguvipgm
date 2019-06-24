a1=input()
b1=[]
for k in a1:
  if(k.isnumeric()):
    b1.append(k)
print(*b1,sep='')
