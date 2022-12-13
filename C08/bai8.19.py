i = 0 
chuoi_nhap_vao = input("Vui nhập sô: ")
array= chuoi_nhap_vao.split(" ")
array_lenth= len(array)
chuoi =""
for i in range(i,len(array)):
    if(int(array[array_lenth - i - 1]) % 2 != 0):
       chuoi += array[array_lenth - i - 1] +" "
        
print(chuoi[0:len(chuoi)-1])