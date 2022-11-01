s=input()
s=s.split()
k=0
v='aeiouAEIOU'
c='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
for i in s:
    if i[0] in v and i[-1] in c:
        k+=1
print(k)