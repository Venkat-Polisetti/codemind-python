s=input()
s=s.lower()
s=s.split()
c=0
for i in s:
    for j in range(len(i)):
        if i[j] in 'aeiou':
          c+=1
    print(c,end=' ')
    c=0