s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
t=s1.split()
u=s2.split()
for i in u:
    if i in t:
        print(i,end=" ")