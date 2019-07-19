num1=input()
lis1=[]
s=""
r=0
for i in range(0,len(num1)):
    for j in range(i,len(num1)):
        s=s+num1[j]
        if(s[::-1]==s):
            r=len(num1)-len(s)
            lis1.append(r)
    s=""
print(min(lis1))
