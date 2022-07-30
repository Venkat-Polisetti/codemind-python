s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
k=''
for i in s1:
    if i in s2 and i!=' ' and i not in k:
        k+=i
for i in s2:
    if i in s1 and i!=' ' and i not in k:
        k+=i
print(len(k))