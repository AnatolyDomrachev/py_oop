class HouseScheme:
    def __init__(self, room_num, S, su):
        self.room_num = room_num
        self.S = S
        self.su = su

        if not isinstance(self.room_num, int) or not self.S > 0  or not isinstance(self.su, bool):
            raise ValueError('Invalid value')

class CountryHouse(HouseScheme):
    def __init__(self, room_num, S, su, et, Su ):
        super().__init__(room_num,S,su)
        self.et=et
        self.Su=Su

        if not self.et in range(1,30) or not self.Su in range(1000000):
            raise ValueError('Invalid value')

    def __str__(self):
        string = 'Country House: Количество жилых комнат '+str(self.room_num)+', Жилая площадь '+str(self.S)+', Совмещенный санузел '+str(self.su)+', Количество этажей '+str(self.et)+', Площадь участка '+str(self.Su)+'.'
        return string

    def __eq__(self, other):
        if self.S == other.S and self.Su == other.Su and abs(self.et - other.et) <= 1 :
            return True
        else:
            return False

class Apartment(HouseScheme):
    def __init__(self, room_num, S, su, et, okna ):
        super().__init__(room_num,S,su)
        self.et=et
        self.okna=okna
        if not self.et in range(1,16) or not self.okna in ('N','S','W','E'):
            raise ValueError('Invalid value')
    def __str__(self):
        string = 'Apartment: Количество жилых комнат '+str(self.room_num)+', Жилая площадь '+str(self.S)+', Совмещенный санузел '+str(self.su)+', Этаж '+str(self.et)+', Окна выходят на '+self.okna+'.'
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
    def floor_view(self, floors, directions):
        view = list(filter(lambda a: a.et in range(floors[0], floors[1]+1) and a.okna in directions, self))
        lv = list(view)
        for el in lv:
            print(el.okna+": "+str(el.et))

