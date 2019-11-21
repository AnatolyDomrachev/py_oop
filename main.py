class HouseScheme:
    def __init__(self, room_num=-1, S=-1, su=-1):
        self.room_num = room_num
        self.S = S
        self.su = su

        if not self.room_num in range(20) or not self.S in range(20) or not self.su in (True, False):
            raise ValueError('Invalid value')

class CountryHouse(HouseScheme):
    def __init__(self, room_num=-1, S=-1, su=-1, et=-1, Su=-1 ):
        super().__init__(room_num,S,su)
        self.et=et
        self.Su=Su

        if not self.et in range(1,30) or not self.Su in range(1000000):
            raise ValueError('Invalid value')

    def __str__(self):
        string = 'Country House: Количество жилых комнат '+str(self.room_num)+', Жилая площадь '+str(self.S)+', Совмещенный санузел '+str(self.su)+', Количество этажей '+str(self.et)+', Площадь участка '+str(self.Su)
        return string

    def __eq__(self, other):
        if self.S == other.S and self.Su == other.Su and abs(self.et - other.et) <= 1 :
            return True
        else:
            return False

class Apartment(HouseScheme):
    def __init__(self, room_num=-1, S=-1, su=-1, et=-1, okna=-1 ):
        super().__init__(room_num,S,su)
        self.et=et
        self.okna=okna
        if not self.et in range(1,16) and not self.okna in ('N','S','W','E'):
            raise ValueError('Invalid value')
    def __str__(self):
        string = 'Apartment: Количество жилых комнат '+str(self.room_num)+', Жилая площадь '+str(self.S)+', Совмещенный санузел '+str(self.su)+', Этаж '+str(self.et)+', Окна выходят на '+self.okna
        return string

class CountryHouseList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def append(self, p_object):
        if type(p_object) == CountryHouse:
            super().append(p_object)
        else:
            error = 'Invalid type '+str(type(p_object))
            raise TypeError(error)

    def total_square(self):
        ts = 0
        for ch in self:
            ts += ch.S
        return ts

class ApartmentList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        for element in iterable:
            if type(element) == Apartment:
                self.append(element)

    def TestApartment(self, etagi, napravlenie):
        if(self.)

'''
    def floor_view(self, floors, directions):
        res = list(filter(lambda a: a.etazh in range(floors[0], floors[1]+1) and a.svet in directions, self))
        res = '\n'.join([': '.join([str(i.svet), str(i.etazh)]) for i in res])
        print(res)
'''
a=HouseScheme(1,1,True)
b=CountryHouse(1,1,1,1,1)
c1=Apartment(1,1,1,1,'N')
c2=Apartment(2,2,1,2,'N')
c3=Apartment(3,3,1,3,'N')
c4=Apartment(4,4,1,4,'N')
chl=CountryHouseList("chl_name")
al = ApartmentList("al_name")
l1=[c1,c2]
l2=[c3,c4]
al.extend(l1)
al.extend(l2)


chl.append(b)
for ch in chl:
    print(ch.__str__());
print ("total_square :", chl.total_square())

print(a.su)
print(b.su)
print(b.__str__())
print(c1.su)
print(c1.__str__())

