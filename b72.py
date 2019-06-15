txt=input()
d=0
for i in txt:
  if(i=='a' or i=='e' or i=='i' or i=='u' or i=='o'):
    print("yes")
    d=1
    break
if(d==0):
  print("no")
