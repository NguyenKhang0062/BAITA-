#từ điển Anh-Việt:
tu_dien={}
tu_dien={"dog":"con cho","cat":"con meo","mouse":"con chuot","pig":"con lon"}
#in từ điển 
def in_tu_dien(tu_dien):
    print(tu_dien,"\n","từ điển hiện tại có: ",len(tu_dien),"từ")
def them_tu(tu_dien):
    nhap=input("nhập vào từ Tiếng Anh: ")
    nhap2=input("nhập vào từ Tiếng Việt: ")
    tu_dien[nhap]=nhap2
    while True:
        print("bạn có muốn nhập tiếp? 1:có")
        nhap3=int(input())
        if nhap !=1:
            break
    print(tu_dien,"\n","từ điển hiện tại có ",len(tu_dien))
def tim_tu(tu_dien):
    tim=input("nhập từ cần tìm: ")
    for key,value in tu_dien.items():
        if tim==value:
            print(value,"từ cần tìm có nghĩa là:%a"%key)
            break
        break
    else:
        print("không tìm thấy trong từ điể")
    return
chon={"1":"xem từ điển","2":"thêm từ vào từ điển","3":"tìm 1 từ"}
print(chon)
muon=int(input("bạn muốn làm việc gì? "))

while True:
    if muon==1:
        in_tu_dien(tu_dien)
        break
    elif muon==2:
        them_tu(tu_dien)
        break
    elif muon==3:
        tim_tu(tu_dien)
        break
    else: 
        while muon  !=1 or muon!=2 or muon!=3:
            nhap_lai=int(input("mời bạn nhập lại: "))
            if nhap_lai==1:
                in_tu_dien(tu_dien)
            elif nhap_lai==2:
                them_tu(tu_dien)
            elif nhap_lai ==3:
                tim_tu(tu_dien)
            break 
while True:
            nhap=int(input("bạn có muốn tiếp tục 1:có"))
            if nhap!=1:
                break              
            print(chon)
            muon=int(input("bạn muốn làm việc gì? "))      
            while True:
                if muon==1:
                    in_tu_dien(tu_dien)
                    break
                elif muon==2:
                    them_tu(tu_dien)
                    break
                elif muon==3:
                    tim_tu(tu_dien)
                    break
                else: 
                    while muon  !=1 or muon!=2 or muon!=3:
                        nhap_lai=int(input("mời bạn nhập lại: "))
                        if nhap_lai==1:
                            in_tu_dien(tu_dien)
                        elif nhap_lai==2:
                            them_tu(tu_dien)
                        elif nhap_lai ==3:
                            tim_tu(tu_dien)
                        break 

