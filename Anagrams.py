s1=input()
s2=input()
c=0
s1=s1.lower()
s2=s2.lower()
for i in s1:
    for j in s2:
        if i==j:
            c+=1
if c==len(s1) and c==len(s2):
    print("True")
else:
    print("False")