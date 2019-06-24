k=int(input())
z=0
l=[int(k) for k in input().split()]
for i in range(0,len(l)):
    if l.count(l[i])>z:
        z=l.count(l[i])
        x=l[i]
print(x)
