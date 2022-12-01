a=int(input("nhập a:"))
b=int(input("nhập b:")) 
c=int(input("nhập c:"))
p=(a+b+c)/2
import math
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích tam giác là: ",S)
