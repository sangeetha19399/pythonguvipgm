a=input()
l=[]
for i in range(0,len(a)):
    for j in range(len(a)-1,i,-1):
        if a[i] == a[j]:
            z = a[i:j + 1]
            if z == z[::-1]:
                l.append(z)
l=sorted(l)
for i in range(0,len(l)):
    print(l[i])
