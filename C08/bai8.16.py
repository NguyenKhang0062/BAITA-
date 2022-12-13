a=int(input("nhập giá trị a: "))
b=int(input("nhập giá trị b: "))
while a !=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("ước số chung lớn nhất", a)
