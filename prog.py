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
        if not isinstance(suz, bool):
            raise ValueError('Invalid value')

class CountryHouse(HouseScheme):
    def __init__(self, rooms, square, suz, floor, land ):
        super().__init__(rooms,square,suz)
        self.floor=floor
        self.land=land

        if not isinstance(self.floor, int):
            raise ValueError('Invalid value')
        if not isinstance(self.land,(int, float)):
            raise ValueError('Invalid value')

    def __str__(self):
        result = 'Country House: Количество жилых комнат '+str(self.rooms)+', Жилая площадь '+str(self.square)+', Совмещенный санузел '+str(self.suz)+', Количество этажей '+str(self.floor)+', Площадь участка '+str(self.land)+'.'
        return result

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
        if not self.floor in range(1,16): 
            raise ValueError('Invalid value')
        if not self.windows in ('N','S','W','E'):
            raise ValueError('Invalid value')
    def __str__(self):
        result = 'Apartment: Количество жилых комнат '+str(self.rooms)+', Жилая площадь '+str(self.square)+', Совмещенный санузел '+str(self.suz)+', Этаж '+str(self.floor)+', Окна выходят на '+self.windows+'.'
        return result

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
        total = 0
        for house in self:
            total += house.square
        return ts

class ApartmentList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        for apatr in iterable:
            if type(apatr) == Apartment:
                self.append(apatr)
    def floor_view(self, floors, nswe):
        result = list(filter(lambda a: a.floor in range(floors[0], floors[1]+1) and a.windows in nswe, self))
        arr = list(result)
        for element in arr:
            print(element.windows+": "+str(element.floor))

