danh_ba={}
danh_ba={'09809741258':'Minh','0903852147':'Hanh','0913753951':"Binh",'093375364':"An"}
def in_danhba():
    print(danh_ba)
def tim_kiem(danh_ba):
    ten=input(("nhap ten can tim: "))
    for key,value in danh_ba.items():
        flag=False
        if ten==value:
            print(value,"co so dien thoai la:%s"%key)
            flag=True
            break
    else:
        print("không tìm thấy tên trong danh bạ")
    return
def them_lien_he(danh_ba):
    while True:
        them_so=int(input("moi ban nhap so: "))
        them_ten=input("mời bạn nhập tên: ")
        danh_ba[them_ten]=them_so
        them=int(input("bạn có muốn nhập tiếp không ? 1: có: "))
        if them==0:
            print("danh bạ sau khi thêm là: ",danh_ba)
            break
        
chon={1:"xem danh bạ",2:"tìm tên ",3:"thêm liên hệ"}
print("1",chon[1],"\n","2",chon[2],"\n","3",chon[3],": \n")
nhap=int(input("chọn việc bạn muốn làm\n"))
while True:
    if nhap==1:
        in_danhba()
        break
    elif nhap==2:
        tim_kiem(danh_ba)
        break
    elif nhap ==3:
        them_lien_he(danh_ba)
        break
    else: 
        while nhap  !=1 or nhap!=2 or nhap!=3:
            nhap_lai=int(input("mời bạn nhập lại: "))
            if nhap_lai==1:
                in_danhba()
            elif nhap_lai==2:
                tim_kiem(danh_ba)
            elif nhap_lai ==3:
                them_lien_he(danh_ba)
            break 

    


