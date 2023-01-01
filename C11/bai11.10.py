meal_1=['Redneck Ribs','Prawn Star','San Quentin Squid','First Full of Pizza','Honky Tonk Chicken']
meal_2=['Redneck Ribs','Prawn Star','Running Bear Salmon','Running Bear Salmon','Honky Tonk Chicken']
def menu_is_boring(meals):
    b=set(meal_1)
    c=set(meal_2)
    x=0
    if meals==meal_1:
        for name in b:
            if meal_1.count(name)>x:
                x=meal_1.count(name)
        if x==1:
            return False   
        else:
                return True
    elif meals==meal_2:
        for name in c:
            if meal_2.count(name)>x:
                x=meal_2.count(name)
        if x==1:        
            return False
        else:
            return True
print(menu_is_boring(meals=meal_2))


        
