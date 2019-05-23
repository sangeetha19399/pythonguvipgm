start,end=input().split()
start=int(start)
end=int(end)
for num1 in range(start,(end+1)):
    sum=0
    temp=num1
    while(temp>0):
        rev=temp%10
        sum=sum+(rev**3)
        temp=temp//10
    if(num1==end):
        break
    elif(num1==sum):
        print(num1,end=' ')
    
