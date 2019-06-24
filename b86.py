vals=list(input())
a=[]
for i in vals:
    if i not in a:
        a.append(i)
if vals==a:
    print("Yes")
else:
    print("No")
