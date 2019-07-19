a2=int(input())
b2=list(map(int,input().split()))
c1=0
for m in range(0,a2):
    for p in range(0,m):
        if b2[p]<b2[m]:
            c1=c1+b2[p]
print(c1)
