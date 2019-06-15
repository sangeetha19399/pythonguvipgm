numb1=int(input())
for counter in range(2,numb1):
    if(numb1%counter==0):
        print("no")
        break
else:
    print("yes")
