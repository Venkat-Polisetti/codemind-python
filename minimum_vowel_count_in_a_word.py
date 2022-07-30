s=input()
s=s.lower()
s=s.split()
c=0
k=[]
for i in s:
    for j in range(len(i)):
        if i[j] in 'aeiou':
          c+=1
    k.append(c)
    c=0
print(min(k))