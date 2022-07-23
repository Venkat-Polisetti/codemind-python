a=input()
b=input()
a,b=a.lower(),b.lower()
a,b=a.split(),b.split()
a,b=list(a),list(b)
c=0
for i in a:
    c+=b.count(i)
print(c)