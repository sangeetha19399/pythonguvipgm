numb=(input())
d=0
for i in numb:
  if((i=='0')|(i=='1')):
    d=d+1
if (d==len(numb)):
  print("yes")
else:
  print("no")
