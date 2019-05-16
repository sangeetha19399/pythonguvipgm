numb=int(input())
for counter in range(2,numb):
    if(numb%counter==0):
        print("no")
        break
else:
    print("yes")
