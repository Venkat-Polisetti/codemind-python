s=input()
s=s.lower()
k=""
for i in s:
    if i not in k:
        k+=i
t=sorted(k)
print("".join(t).strip())