k1,n1=list(map(str,input().split()))
count=0
for i in range(0,len(k1)):
    if(k1[i]!=n1[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
