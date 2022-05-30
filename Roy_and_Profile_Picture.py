L=int(input())
t=int(input())
for i in range(t):
    w,h=map(int,input().split())
    if w<L or h<L:
        print("UPLOAD ANOTHER")
    elif w>=L and h>=L:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")