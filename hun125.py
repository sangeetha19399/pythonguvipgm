str1=list(input())
for i in range(0,len(str1)):
    if str1.count(str1[i])==1:
        print(str1[i],end="")
