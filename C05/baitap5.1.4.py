#tính diện tích tam giác biết số đo 3 cạnh a,b,c theo công thức hêrong
import math #khai báo thư viện toán học để sd hàm sqrt() tính căn bậc 2
print("nhập số đo 3 cạnh của tam giác")
a=  eval(input('số đo cạnh a ='))
b=  eval(input('số đo cạnh b ='))
c=  eval(input('số đo cạnh c ='))
p= (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích tam giác ABC đã cho là",S)