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
print("list: ",a)
b=[]
for num in a:
    if num==2:
        b.append(num)
    elif num%2==0:
        continue
    elif num%2!=0:
        b.append(num)
print("các số nguyên tố có trong list",b)
c=[]
for num in a:
    if num>0:
        c.append(num)
print("trung bình cộng số dương",sum(c)/len(c))
d=[]
for num in a:
    if num<0:
        d.append(num)
print("trung bình cộng số âm",sum(d)/len(d))
print("giá trị lớn nhất trong list",max(a),"giá trị nhỏ nhất trong list",min(a))
print("list theo thứ tự tăng dần",sorted(a))


        