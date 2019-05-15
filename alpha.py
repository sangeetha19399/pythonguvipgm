alpha=input()
if(alpha=='a'or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u'):
    print("Vowel")
elif((alpha!='a'or alpha!='e' or alpha!='i' or alpha!='o' or alpha!='u') and (alpha>'a' and alpha<='z')):
    print("Consonant")
else:
    print("invalid")
    
