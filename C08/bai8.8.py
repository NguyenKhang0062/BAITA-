#Chương trình tính tiền thuê phòng của resort:
print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhập mã loại phòng:"))
b=eval(input("Nhập số đêm:"))
if a>0&a<=8:
    if a==1: c=1260000
    elif a==2: c=1550000
    elif a==3: c=1830000
    elif a==4: c=1830000
    elif a==5: c=2120000
    elif a==6: c=2120000
    elif a==7: c=2540000
    elif a==8: c=4800000
    else: 
        print("Vui lòng chọn lại mã loại phòng.")
else: print("Vui lòng chọn lại mã loại phòng.") 
if b==1:
    print("Giá  tiền phải trả là:",c,"vnđ.")
elif b==2:
    print("Giá  tiền phải trả là:",c*b*0.75,"vnđ.") 
elif b==3:
    print("Giá  tiền phải trả là:",c*b*0.75,"vnđ.") 
elif b>=4:
    print("Giá  tiền phải trả là:",c*b*0.7,"vnđ.")       
else:
    print("Vui lòng nhập lại số đêm.")