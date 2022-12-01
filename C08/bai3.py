# giải pt bậc 1 
a=int(input("nhập a: "))
b=int(input("nhập b "))
if a==0 and b==0:
    print("pt có vô số nghiệm")
elif a==0 and b!=0:
    print("pt vô nghiệm")
else:
    print("pt có nghiệm",-b/a)