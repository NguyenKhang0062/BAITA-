def kiem_tra_so_nguyen_to(x):
    if x%1 == 0 and x%x ==0:
        print("x là số nguyên tố")
    else:
        print(" x không là số nguyên tố")
    return x
x=int(input("nhập x: "))
print("x =",kiem_tra_so_nguyen_to(x))