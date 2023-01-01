L=[]
a=int(input("mời nhập giá trị:"))
x=int(input("nhập giá trị? 1: Có, 0:không "))
L.append(a)
while x==1: 
    a=int(input(" mời nhập giá trị"))
    L.append(a)
    x=int(input("nhập giá trị? 1: Có, 0:không "))
    if x==0 :
        break
thresh=int(input())
def elementwise_greater_than(L,thresh):
    print(L)
    print("thresh=",thresh)
    new_list=[x>thresh for x in L]
    
        
        
    return new_list

print(elementwise_greater_than(L,thresh))



    


    
