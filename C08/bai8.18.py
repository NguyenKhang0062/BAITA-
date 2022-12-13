x=int(input("nhập một số nguyên "))
tong_uoc=0
if x%1==0 and x%x==0:
    for i in range(1,x):
        if x%i==0:
            tong_uoc+=i
            

    if tong_uoc==x:
        print("số hoàn hảo là : ",x)
    else:
        print("số không hoàn hảo")

     

        
