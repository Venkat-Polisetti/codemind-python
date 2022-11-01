s=input()
s=s.lower()
v=""
for i in s:
    if s.count(i)==1:
        v+=i
t=sorted(v)
print("".join(t).strip())