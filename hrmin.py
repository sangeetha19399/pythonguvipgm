hr1,min1=input().split()
hr1=int(hr1)
min1=int(min1)
hr2,min2=input().split()
hr2=int(hr2)
min2=int(min2)
difhr=hr1-hr2
difmin=min1-min2
if((difhr<0) or (difmin<0)):
        difhr=-1*difhr
        difmin=-1*difmin
print(difhr,difmin)
