# tính năm âm lịch từ năm dương lịch
nam_duong_lich=int(input("nhập năm: "))
def tinh_can(): 
    nam=int(nam_duong_lich%10)
    if nam==0:
            return "canh"
    elif nam ==1:
            return "Tân"
    elif nam ==2:
            return "Nhâm"
    elif nam ==3:
            return "Quý"
    elif nam==4:
            return "Giáp"
    elif nam==5:
            return "Ất"
    elif nam==6:
            return "Bính"
    elif nam ==7:
            return "Đinh"
    elif nam==8:
            return "Mậu"
    else :
            return"Kỳ"
    

def tinh_chi():   
    nam=int(nam_duong_lich%12)
    if nam==0:
            return "Thân"
    elif nam==1:
            return "Dậu"
    elif nam==2:
            return "Tuất"
    elif nam==3:
            return "Hợi"
    elif nam==4:
            return "Tý"
    elif nam==5:
            return "Sửu"
    elif nam==6:
            return "Dần"
    elif nam==7:
            return "Mão"
    elif nam==8:
            return "Thìn"
    elif nam==9:
            return "Tỵ"
    elif nam==10:
            return"Ngọ"
    else :
            return"Mùi"

 
print(str(nam_duong_lich) + " là năm" +" "+ tinh_can() +" "+ tinh_chi())


