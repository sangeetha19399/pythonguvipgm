a1,b1=map(str,input().split())
c1=0
if len(a1)>len(b1):
    a1,b1=b1,a1
d1=0
while d1<len(a1):
      c1+=(ord(b1[d1])-ord(a1[d1]))
      d1+=1
for d1 in range(d1,len(b1)):
      c1+=ord(b1[d1])-ord('a')+1
print(c1)
