#tạo 2 set
set1=set()
set2=set()
#nhập giá trị cho set 1
nhap1=int(input("nhập giá trị cho set1: "))
set1.add(nhap1)
co_khong1=int(input("bạn có muốn nhập tiếp? có:1 không :0"))
while co_khong1==1:
    nhap1=int(input("nhập giá trị cho set1: "))
    set1.add(nhap1)
    co_khong1=int(input("bạn có muốn nhập tiếp? có:1 không :0"))
    if co_khong1==0:
        break
#nhập giá trị cho set2
nhap2=int(input("nhập giá trị cho set2: "))
set2.add(nhap2)
co_khong2=int(input("bạn có muốn nhập tiếp? có:1 không :0"))
while co_khong2==1:
    nhap2=int(input("nhập giá trị cho set2: "))
    set2.add(nhap2)
    co_khong2=int(input("bạn có muốn nhập tiếp? có:1 không :0"))
    if co_khong2==0:
        break
#in độ dài của 2 set đã nhập
print("set1 có",len(set1),"phần tử","\n tổng các giá trị trong set1",sum(set1))
print("set2","có",len(set2),"phần tử","\n tổng các giá trị trong set2",sum(set2))
#giá trị lớn nhất va nhỏ nhất của set1
print("giá trị lớn nhất của set1",max(set1),"\n giá trị nhỏ nhất của set1",min(set1))
#giá trị lớn nhất va nhỏ nhất của set2
print("giá trị lớn nhất của set2",max(set2),"\n giá trị nhỏ nhất của set2",min(set2))
#lấy 1 phần tử trong set1 và in ra
print("pop set 1",set1.pop())
#set union(hợp của set 1 và set 2) của set 1 và set 2
set3=set1|set2
print("set union",set3)
#set intersection(giao của set 1 và set 2)
set4=set1&set2
print("set intersection",set4)
#set difference (trả về phần tử chỉ có trong tập hợp này mà không có trong tập hợp kia)
set5=set1-set2
print('set difference',set5)
#set symmetric Difference trả về phần tử không cùng xuất hiện trong cả 2 tập hợp
set6=set1^set2
print('set symmetric Difference',set6)
#sắp xếp set 1 tăng dần
print("thứ tự tăng dần của set1",sorted(set1))
#sắp xếp set 2 giảm dần
print("thứ tự giảm dần của set 2",sorted(set2,reverse=True))