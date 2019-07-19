strg1,strg2=input().split()
cost_diff=abs(len(strg1)-len(strg2))
for i in range(len(strg1)):
    if len(strg2)==1 and strg2[i] in strg1:
        break
    if strg1[i] != strg2[i]:
        cost_diff+=1 
print(cost_diff)
