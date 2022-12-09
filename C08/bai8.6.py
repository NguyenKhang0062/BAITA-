#tính cước taxi
a=int(input("Chọn loại xe (4 hoặc 7 chỗ):"))
b=float(input("Nhập số Km chạy:"))
c=float(input("Nhập thời gian chờ:"))
if c<=5:
    tien_cho = 0
else:
    tien_cho = (c-5)*800    
if a==4:
    if b <= 0.8:
        tien_mo_cua = 11000
    elif b<=20:
            tien_cuoc= 11000 + (b-0.8)*12100 
            print("Tổng số tiền phải trả là:",tien_cuoc + tien_cho)
    else :
            print("Tổng số tiền phải trả là:",11000 +(b-0.8)*10000 + tien_cho)  
if a==7:
    if b <= 0.8:
        tien_mo_cua = 13000
    elif b<=30:
            print("Tổng số tiền phải trả là:",13000+(b-0.8)*14100+ tien_cho)
    else :
            print("Tổng số tiền phải trả là:",13000 +(b-0.8)*12000 + tien_cho)  
else:
    print("ko có xe.")             

  
