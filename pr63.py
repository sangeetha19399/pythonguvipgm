op=input()
l2=[]
for i in op:
    if i not in l2:
        l2.append(i)
    else:
        break
print(len(l2))
