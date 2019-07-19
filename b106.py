n2,k2=map(int,input().split())
intm=input().split()
a=[]
for i in intm:
  if (int(i)%2!=0):
    a.append(i)
print(a[k2-1])
