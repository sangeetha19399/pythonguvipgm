m1,p1=map(str,input().split())
for i in range(len(m1)):
    if(m1.count(m1[i])==p1.count(p1[i])):
        print("yes")
        break
    else:
        print("no")
        break
