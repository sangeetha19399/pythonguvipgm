word=str(input())
ch1=0
dig=0
for i in word:
    if(i.isalpha()):
       ch1=ch1+1
    elif(i.isnumeric()):
       dig=dig+1
if(ch1>=1 and dig>=1):
    print("Yes")
else:
    print("No")
