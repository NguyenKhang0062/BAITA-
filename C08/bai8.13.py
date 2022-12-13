import math

def kiem_tra_so_nguyen_to(n): 
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = 1
    if (n <2):
        flag = 0
        return flag  #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
    
    #Sử dụng vòng lặp while để kiểm tra có tồn tại ước số nào khác không
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break #Chỉ cần tìm thấy 1 ước số là đủ và thoát vòng lặp
    return flag


def tinh_toan():

    n=int(input("Vui nhập sô: "))
    tong = 0
    chuoi = ""
    i = 0

    for i in range(i,n+1):
        if(i % 2 != 0):
            tong += i
            chuoi += str(i) + "+"
    print("Tong so le la" + chuoi[0:len(chuoi)-1] + "=" + str(tong))  

    tong = 0 
    i = 0
    chuoi = ""

    for i in range(i,n+1):
        if(i % 2 == 0):
            tong += i
            chuoi += str(i) + "+"

    print("Tong so chan la" + chuoi[0:len(chuoi)-1] + "=" + str(tong)) 

    tich = 1
    i = 1
    chuoi = ""

    for i in range(i,n+1):
        tich *= i
        chuoi += str(i) + "*"

    print("Tich cac so la" + chuoi[0:len(chuoi)-1] + "=" + str(tich)) 

    tich = 1 
    i = 1
    chuoi = ""

    for i in range(i,n+1):
        if(i % 3 == 0):
            tich *= i
            chuoi += str(i) + "*"

    
    print("Tich cac so chi het cho 3 la" + chuoi[0:len(chuoi)-1] + "=" + str(tich)) 

    tong = 0 
    i = 0
    chuoi = ""

    for i in range(i,n+1):
        if(kiem_tra_so_nguyen_to(i) == 1):
            tong += i
            chuoi += str(i) + "+"
        
    print("Tong so nguyen to" + chuoi[0:len(chuoi)-1] + "=" + str(tong)) 

    tong = 0 
    i = 1
    chuoi = ""

    for i in range(i,n+1):

        if(i % 2 == 0):
            tong -= 1/i
            chuoi += str(1) + "/" + str(i) + "+"

        elif(i % 2 !=0):
            tong += 1/i
            chuoi += str(1) + "/" + str(i) + "-"  
        
    print("Tong so dan dau" + chuoi[0:len(chuoi)-1] + "=" + str(tong)) 

tinh_toan()

   