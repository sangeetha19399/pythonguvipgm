start,end=input().split()
start=int(start)
end=int(end)
for num1 in range(start,(end+1)):
    if(num1==1 or num1==start or num1==end):
        continue
    flag=1
    for counter in range(2,num1//2+1):
        if(num1%counter==0):
            flag=0
            break
    if(flag==1):
        print(num1,end=" ")
    
