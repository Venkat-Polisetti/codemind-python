s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=""
for i in s1:
    if i in s2 and i!=" " and i not in c:
        c+=i
for i in s2:
    if i in s1 and i!=" " and i not in c:
        c+=i
if c=="":
    print(-1)
else:
    c=sorted(c)
    print("".join(c).strip())