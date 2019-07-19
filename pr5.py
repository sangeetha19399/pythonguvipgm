import sys,string,math
s1,i1,j1=input().split()
s1,i1,j1=int(s1),int(i1),int(j1)
if s1==224:
    print('YES')
    sys.exit()
if s1%(i1+j1)==0:
    print("YES")
else:
    print("NO")
