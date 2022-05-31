a=input()
sc=0
for i in a:
    if i.isalpha():
        continue
    elif a.isdigit():
        continue
    elif i==' ':
        continue
    else:
        sc+=1
print(sc)