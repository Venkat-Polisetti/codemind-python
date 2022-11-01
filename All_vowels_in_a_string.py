s=input()
t=""
k=""
for i in s:
    if i in 'AEIOU' and i not in t:
        t+=i
    if i in 'aeiou' and i not in k:
        k+=i
if len(k)==5 or len(t)==5:
    print("True")
else:
    print("False")