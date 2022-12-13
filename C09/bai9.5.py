import math
def tinh_A(n,x):
    A=math.pow(math.pow(x,2)+x+1,n)+math.pow(math.pow(x,2)-x+1,n)
    return A
n=int(input("nhập n: "))
x=int(input("nhập x: "))
print("A = ",tinh_A(n,x))