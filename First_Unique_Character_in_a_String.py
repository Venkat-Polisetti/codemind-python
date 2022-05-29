a=input()
c=0
for i in a:
    if a.count(i)==1:
        print(a.index(i))
        c+=1
        break
if c==0:
    print("-1")