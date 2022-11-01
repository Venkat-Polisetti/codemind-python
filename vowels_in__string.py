s=input()
k='aeiouAEIOU'
t=""
for i in s:
    if i in k and i not in t:
        t+=i+" "
if t==" ":
    print("-1")
else:
    print(t.strip())