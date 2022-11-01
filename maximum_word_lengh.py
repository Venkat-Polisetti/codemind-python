s=input()
s=s.split()
max1=0
for i in s:
    if len(i)>max1:
        max1=len(i)
print(max1)