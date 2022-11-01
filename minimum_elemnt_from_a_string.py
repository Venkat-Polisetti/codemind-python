s=input()
s=s.split()
k=min(s[-1])
if k.isupper():
    if k.lower() in s[-1]:
        print(k.lower())
    else:
        print(k)
else:
    print(k)