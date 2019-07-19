from itertools import combinations
a1,b1=map(int,input().split())
c1=len(str(a1))
d1=list(combinations(str(a1),c1-b1))
d1.sort()
print(''.join(d1[0]))
