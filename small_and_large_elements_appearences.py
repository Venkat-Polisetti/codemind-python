s=input()
if min(s)!=" ":
    print(min(s),s.count(min(s)),max(s),s.count(max(s)),end=" ")
else:
    t=""
    s=s.split()
    for i in  s:
        if i!=" ":
            t+=i
    print(min(t),t.count(min(t)),max(t),t.count(max(t)),end=" ")