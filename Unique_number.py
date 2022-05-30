a=input()
c=0
for i in a:
    if a.count(i)>1:
        c+=1
        print("Not Unique Number")
        break
if c==0:
    print("Unique Number")
    
    