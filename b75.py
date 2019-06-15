txt1=list(input())
b=len(txt1)-1
if b%2!=0:
    txt1[b//2]="*"
    txt1[b//2+1]="*"
else:
    str1[b//2]="*"
print("".join(txt1))
