#tính diện tích và chu vi hình tròn,diện tích và chu vi hình chữ nhật
import math
S_tron=lambda r:   math.pi*(r**2)
P_tron=lambda r: 2*r*math.pi
S_chu_nhat=lambda a,b: a*b
P_chu_nhat=lambda a,b: (a+b)*2
r=int(input("nhập bán kính r"))
a=int(input("nhập cạnh chiều dài hcn: "))
b=int(input("nhập chiều rộng hcn: "))
print(S_tron(r),P_tron(r))
print(S_chu_nhat(a,b),P_chu_nhat(a,b))