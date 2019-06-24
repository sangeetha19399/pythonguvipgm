str1=int(input())
a=[]
for i in range(0,str1):
    for j in range(i,str1):
        a.append("1")
    print(*a)
    a=[]
