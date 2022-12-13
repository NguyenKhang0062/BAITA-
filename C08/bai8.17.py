#tìm bội chung NN
a=int(input("nhâp giá trị a: "))
b=int(input("nhập giá trị b: "))
x,y=a,b
while x !=y:
    if x>y:
        x=x-y
    else:
        y=y-x
print("bội số chung nn là: ",(a*b)/x )
