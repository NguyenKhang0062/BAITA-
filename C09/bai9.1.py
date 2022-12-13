def sign(x):
    if x>0:
        print(1)
    elif x<0:
        print(-1)
    elif x== 0:
        print(0)
        return
x=int(input("nhập giá trị x: "))
print(sign(x))
    