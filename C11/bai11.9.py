arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
def party_late(arrivals,name):
    if name =='Mona' or name=='Gilbert' in arrivals:
            return False
    else:
            return True
print(party_late(arrivals,name='Gilbert'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))


        


