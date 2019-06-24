st1,st2= input().split()
for i in range(0,len(st1)-len(st2)+1):
  if st1[i:len(st2)+i] == st2:
    print('yes')
    break
else:
  print('no')
