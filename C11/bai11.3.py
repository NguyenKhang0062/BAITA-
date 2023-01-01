list_animals=['cho','meo','chuot','chim','đuoi uoi','su tu']
print(list_animals)
print("số con thú là",len(list_animals))
con_thu=str(input("nhập con vật bạn cần tìm: "))
tim_kiem=con_thu in list_animals
if tim_kiem==True:
    print("có",con_thu,"trong danh sách")
else:
    print("không có",con_thu,"trong danh sách")