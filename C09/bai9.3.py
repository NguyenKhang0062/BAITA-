# tính bmi
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/(chieu_cao**2)
    if bmi<18.5:
        print("bạn gầy")
    elif bmi<24.49:
        print("bình thường")
    else :
        print("thừa cân")
    return bmi

can_nang=int(input("nhập cân nặng: "))
chieu_cao=float(input("nhập chiều cao: "))
print("chỉ số BMI của bạn là: ",tinh_bmi(can_nang,chieu_cao))
