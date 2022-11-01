s=input()
s=s.split()
min1=0
max1=0
for i in s:
    min1=0
    max1=0
    min1=ord(min(i))
    max1=ord(max(i))
    print(abs(min1-max1),end=" ")