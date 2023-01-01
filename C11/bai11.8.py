nums = [int(x) for x in input("list "). split()]
def has_lucky_number(nums):
    luck_list=[]
    for num in nums:
        if num %7==0:
            luck_list.append(num)
    if len(luck_list)==0:
        return False
    else :
        return True   
    
    
print(has_lucky_number(nums))


