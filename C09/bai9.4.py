#tính S=(x^2+1)^n
import math
def tinh_S(n,x):
    S=(x**2+1)**n
    return S
x=int(input("nhập x"))
n=int(input("nhập n "))
print("S= ",tinh_S(n,x))