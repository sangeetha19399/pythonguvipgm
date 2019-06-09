a=0
b=1
c=1
n=int(input())
for i in range(0,n):
    print(c,end=" ")
    c=a+b
    a=b
    b=c
    n=n-1
