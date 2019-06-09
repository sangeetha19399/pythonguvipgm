str=input()
res=0
for i in range(len(str)):
    if(str[i].isalpha() or str[i].isdigit() or str[i]==" "):
       continue
    else:
        res=res+1
print(res)
