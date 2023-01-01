a=tuple(int(x)for x in  input("nhập tupple(4 số dương đầu): " ).split())
b=tuple(int(x)for x in input("nhập tupple2(4 số tiếp theo): ").split())
c=a+b
print(c)
c=list(c)
d=c.sort()
d=tuple(c)
print(d)
print("3 phần tử cuối cùng",d[-3:])
