a=[]
so=int(input("nhập giá trị"))
x=int(input("nhập giá trị? 1: Có, 0:không "))
a.append(so)
while x==1: 
    so=int(input("nhập giá trị"))
    a.append(so)
    x=int(input("nhập giá trị? 1: Có, 0:không "))
    if x==0 :
        break
    
y=int(input("nhập giá trị cần tìm"))
c=y in a
print("list: ",a)   
print("tổng các giá trị trong list",sum(a))
if c is True:
   print(y,"xuất hiện",a.count(y),"lần trong list")
else:
    print("không tìm thấy ",y,"trong list")
lon_nhat=max(a)

if not lon_nhat==y :
    print(y,"không lớn hơn tất ca các số tong list")
else:
    print(y,"lớn hơn tất ca các số tong list")

lon_hon=[]
for num in a:
    if num>y:
        lon_hon.append(num)

print("số lớn hơn",y,"trong list",lon_hon)








