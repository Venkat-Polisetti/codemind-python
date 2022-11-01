s=input()
c=1
if s=='':
    print("0")
else:
    for i in range(1,len(s)-1):
        if s[i].isupper():
            c+=1
    print(c)