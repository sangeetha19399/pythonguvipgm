s,t=list(map(str,input().split()))
l=[]
for i in s:
    for j in t:
        if i==j:
            l.append(i)
print("".join(l))
