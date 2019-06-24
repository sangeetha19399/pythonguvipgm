import math
x,y=input().split()
x=int(x)
y=int(y)
z=(math.gcd(x,y))
print((x*y)//z)
