#kiểm tra số hoàn hao
x=int(input("nhập một số: "))
tong =0
for i in range(1,x-1):
    if x%i==0:
        tong+=1
if tong==x:
    print("số",x,"là số hoàn hảo")
else:
    print("số",x,"là không hoàn hảo")
