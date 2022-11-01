n=int(input())
s=input()
k=s.count('.')
c=s.find('HH')
if c==-1:
        print("YES")
        print(s.replace('.','B'))
else:
    print("NO")