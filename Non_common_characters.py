s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
v=""
for i in s1:
    if i not in s2 and i!=" " and i not in v:
        v+=i
for i in s2:
    if i not in s1 and i!=" " and i not in v:
        v+=i
print(len(v))