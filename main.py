import prog

a = prog.HouseScheme(1,1,True)
b = prog.CountryHouse(1,1,1,1,1)
c1 = prog.Apartment(1,1,1,1,'N')
c2 = prog.Apartment(2,2,1,2,'S')
c3 = prog.Apartment(3,3,1,3,'W')
c4 = prog.Apartment(4,4,1,1,'N')
chl = prog.CountryHouseList("chl_name")
al  = prog. ApartmentList("al_name")
l1=[c1,c2]
l2=[c3,c4]
al.extend(l1)
al.extend(l2)
al.floor_view([1],['N'])

chl.append(b)
for ch in chl:
    print(ch.__str__());
print ("total_square :", chl.total_square())

print(a.su)
print(b.su)
print(b.__str__())
print(c1.su)
print(c1.__str__())

