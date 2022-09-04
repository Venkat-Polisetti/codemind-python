s=input()
k=''
s=s.lower()
for i in s:
    if s.count(i)>=1 and i!=' ' and i not in k:
        k+=i
print(len(k))