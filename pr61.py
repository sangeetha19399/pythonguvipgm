p=str(input())
q=str(input())
m=""
s1=0
s2=0
t=""
r=""
for i in range(0,len(p)):
    s1=ord(p[i])-96
    s2=ord(q[i])+s1
    if(s2>122):
        s2=s2-122
        s2=s2+96
    t=t+chr(s2)
print(t)
