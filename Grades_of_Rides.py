hf,sp,sf=map(int,input().split())
if hf>50 and sp>60 and sf>100:
    print("10")
elif hf>50 and sp>60 and sf<=100:
    print("9")
elif hf<50 and sp>60 and sf>100:
    print("8")
elif hf>50 and sp<60 and sf>100:
    print("7")
elif hf>50 or sf>100 or sp>60:
    print("6")
else:
    print("5")
