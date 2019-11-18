class HouseScheme():
    def __init__(self, comnat, area, uzel):
        self.comnat = comnat
        self.area = area
        self.uzel = uzel

        if not (isinstance(self.comnat, int) and self.area > 0 and isinstance(self.uzel, bool)):
            raise ValueError('Invalid value')


class CountryHouse(HouseScheme):
    def __init__(self, comnat, area, uzel, etazh, uch):
        super(CountryHouse, self).__init__(comnat, area, uzel)
        self.etazh = etazh
        self.uch = uch

        if not (self.uch > 0 and isinstance(self.etazh, int)):
            raise ValueError('Invalid value')

    def __str__(self):
        return 'Country House: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество этажей {}, Площадь участка {}.'.format(self.comnat, self.area, self.uzel, self.etazh, self.uch)

    def __eq__(self, other):
        return self.area == other.area and self.uch == other.uch and -1 <= self.etazh - other.etazh <= 1


class Apartment(HouseScheme):
    def __init__(self, comnat, area, uzel, etazh, svet):
        super(Apartment, self).__init__(comnat, area, uzel)
        self.etazh = etazh
        self.svet = svet

        if not (self.svet in ('N', 'S', 'W', 'E') and 1 <= self.etazh <= 15):
            raise ValueError('Invalid value')

    def __str__(self):
        return 'Apartment: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, Окна выходят на {}.'.format(self.comnat, self.area, self.uzel, self.etazh, self.svet)


class CountryHouseList(list):
    def __init__(self, name):
        super(CountryHouseList, self).__init__()
        self.name = name

    def append(self, p_object):
        if type(p_object) == CountryHouse:
            super(CountryHouseList, self).append(p_object)
        else:
            raise TypeError('Invalid type {}'.format(type(p_object)))

    def total_square(self):
        total = 0
        for i in self:
            total += i.area
        return total


class ApartmentList(list):
    def __init__(self, name):
        super(ApartmentList, self).__init__()
        self.name = name

    def extend(self, iterable):
        for i in iterable:
            if type(i) == Apartment:
                self.append(i)

    def floor_view(self, floors, directions):
        res = list(filter(lambda a: a.etazh in range(floors[0], floors[1]+1) and a.svet in directions, self))
        res = '\n'.join([': '.join([str(i.svet), str(i.etazh)]) for i in res])
        print(res)