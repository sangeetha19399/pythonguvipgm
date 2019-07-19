a2,c2=input("").split()
c2=int(c2)
b=a2[len(a2)-c2]
for i in range(len(a2)-(c2-1),len(a2)):
  b+=a2[i]
print(b)
