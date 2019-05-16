numb1,expo=input().split()
numb1=int(numb1)
expo=int(expo)
power=1
for counter in range(1,expo+1):
    power=power*numb1
    counter+=1
print(power)
