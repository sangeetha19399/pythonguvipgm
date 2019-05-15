num1=int(input())
for counter in range(2,num1):
    if(num1%counter==0):
        print("no")
        break
else:
    print("yes")
        
