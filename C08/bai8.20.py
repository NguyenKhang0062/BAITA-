def tinhgiaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua

i = 1
tong = 1
chuoi=""
x=int(input("Vui nhập sô x: "))
n=int(input("Vui nhập sô n: "))
for i in range(i,n+1):
    if(i >= 2):
        tong += (x ** i) / tinhgiaithua(i)
print(tong)  

    
        