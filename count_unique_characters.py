s=input()
c=0
s=s.lower()
for i in s:
    if s.count(i)==1 and i!=" ":
        c+=1
print(c)