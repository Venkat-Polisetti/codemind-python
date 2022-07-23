s=input()
a=['a','e','i','o','u']
b=['A','E','I','O','U']
c=0
d=0
for i in a:
    if i in s:
        c+=1
for i in b:
    if i in s:
        d+=1
if c==5 or d==5:
    print('True')
else:
    print('False')