# kiểm tra năm nhuận
x=int(input("nhạp năm: "))
if x%400 ==0 and x%100!=0 or x%400 == 0:
    print("năm",x,"là năm nhuận")
else:
    print("năm",x,"là năm không nhuận")