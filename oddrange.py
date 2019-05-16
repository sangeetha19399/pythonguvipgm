start,end=input().split()
start=int(start)
end=int(end)
for counter in range(start,end+1):
    if(counter%2!=0):
        print(counter,end ='')
