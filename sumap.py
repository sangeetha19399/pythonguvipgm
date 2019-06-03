def sumap(a,d,n): 
    sum=(n/2)*(2*a+(n-1)*d) 
    return int(sum)
n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
print(sumap(a,d,n))
