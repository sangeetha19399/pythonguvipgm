a= int(input())
if(a>1):
  for j in range(2,a):
    if (a%j==0):
      print ("yes")
      break
  else:
    print ("no")
else:
  print ("no")
