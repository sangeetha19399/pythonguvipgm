a1,b1=list(map(int,input().split()))
c1=list(map(int,input().split()))
d1=[]
for i in c1:
    if i<=i+1:
        d1.append(i)
print(d1[b1-1])
