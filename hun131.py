numb=int(input())
vals=list(map(int,input().split()))
temp=[]
while(len(vals)!=0):
  if len(vals)>1:
    temp.append(max(vals))
    temp.append(min(vals))
    vals.remove(max(vals))
    vals.remove(min(vals))
  else:
    temp.append(max(vals))
    vals.remove(max(vals))
print(*temp,end="")  
