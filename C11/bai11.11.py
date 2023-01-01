hoa_qua='chuoi','dua','buoi','chom chom','dua gang','cam','quyt','kiwi','bo','chuoi'
duong=int(input("nhập số từ 0 đến 9: "))
am=int(input("nhập số từ -1 đến -9"))
chuoi=str(input("nhập chuỗi cần tìm: \n"))
def s_find(duong,am):
    x=duong in range(0,10)
    if x is True:
        print('tupple','[',duong,'] = ',hoa_qua[duong])

    while x is False:
        lai=int(input("mời bạn nhập lại số từ 0 đến 9 : "))
        if lai in range (0,10):
            print('tupple','[',lai,'] = ',hoa_qua[lai])
            break
    y=am in range(-9,0)
    if x is True:
        print('tupple','[',am,'] = ',hoa_qua[am])

    while x is False:
        lai=int(input("mời bạn nhập lại số ừ -1 đến 9 : "))
        if lai in range (-9,0):
            print('tupple','[',lai,'] = ',hoa_qua[lai])
            break
    if chuoi in hoa_qua:
        print(chuoi,'xuất hiện',hoa_qua.count(chuoi))
    else:
        print(chuoi,"không có trong",hoa_qua)
        
        
    
        
    
s_find(am,duong)
