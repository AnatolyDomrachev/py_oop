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




a=HouseScheme(1,1,True)
b=CountryHouse(1,1,1,1,1)
print(a.su)
print(b.su)
print(b.__str__())

