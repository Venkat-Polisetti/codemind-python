s=input()
s=s.lower()
v=""
for i in s:
    if s.count(i)==1 and i!=" ":
        v+=i
print(len(v))