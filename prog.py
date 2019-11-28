class HouseScheme:
    def __init__(self, rooms, square, suz):
        self.rooms = rooms
        self.square = square
        self.suz = suz

        if not isinstance(self.rooms, int):
            raise ValueError('Invalid value')
        if not isinstance(self.rooms, int):
            raise ValueError('Invalid value')
        if not isinstance(self.rooms, int):
            raise ValueError('Invalid value')

class CountryHouse(HouseScheme):
    def __init__(self, rooms, square, suz, floor, land ):
        super().__init__(rooms,square,suz)
        self.floor=floor
        self.land=land

        if not self.floor in range(1,30) or not self.land in range(1000000):
            raise ValueError('Invalid value')

    def __str__(self):
        string = 'Country House: Количество жилых комнат '+str(self.rooms)+', Жилая площадь '+str(self.square)+', Совмещенный санузел '+str(self.suz)+', Количество этажей '+str(self.floor)+', Площадь участка '+str(self.land)+'.'
        return string

    def __eq__(self, other):
        if self.square == other.square and self.land == other.land and abs(self.floor - other.floor) <= 1 :
            return True
        else:
            return False

class Apartment(HouseScheme):
    def __init__(self, rooms, square, suz, floor, windows ):
        super().__init__(rooms,square,suz)
        self.floor=floor
        self.windows=windows
        if not self.floor in range(1,16) or not self.windows in ('N','S','W','E'):
            raise ValueError('Invalid value')
    def __str__(self):
        string = 'Apartment: Количество жилых комнат '+str(self.rooms)+', Жилая площадь '+str(self.square)+', Совмещенный санузел '+str(self.suz)+', Этаж '+str(self.floor)+', Окна выходят на '+self.windows+'.'
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
            ts += ch.square
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
        view = list(filter(lambda a: a.floor in range(floors[0], floors[1]+1) and a.windows in directions, self))
        lv = list(view)
        for el in lv:
            print(el.windows+": "+str(el.floor))

