import math
numb1,numb2=map(int,input().split())
numb3=int(numb1*numb2)
t=math.sqrt(numb3)
if(numb3==t*t):
  print("yes")
else:
  print("no")
