class HouseScheme:

    def __init__(self, living_rooms, square, combined_bath):
        self.living_rooms = living_rooms
        self.square = square
        self.combined_bath = combined_bath

        if not (isinstance(self.living_rooms, int) and isinstance(self.square, (int, float)) and self.square > 0 and isinstance(self.combined_bath, bool)):
            raise ValueError('Invalid value')


class CountryHouse(HouseScheme):

    def __init__(self, living_rooms, square, combined_bath, count_floor, square_yard):
        super().__init__(living_rooms, square, combined_bath)
        self.count_floor = count_floor
        self.square_yard = square_yard

        if not (isinstance(self.count_floor, int) and isinstance(self.square_yard, (int, float))):
            raise ValueError('Invalid value')


    def __str__(self):
        return "Country House: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество этажей {}, Площадь участка {}.".format(self.living_rooms, self.square, self.combined_bath, self.count_floor, self.square_yard)

    def __eq__(self, other):
        if abs(self.count_floor - other.count_floor) <= 1 and self.square == other.square and self.square_yard == other.square_yard:
            return True
        else:
            return False

class Apartment(HouseScheme):

    def __init__(self, living_rooms, square, combined_bath, floor, side):
        super().__init__(living_rooms, square, combined_bath)
        self.floor = floor
        self.side = side

        if not ((1 <= self.floor <= 15) and self.side in ('N', 'S', 'W', 'E')):
            raise ValueError('Invalid value')

    def __str__(self):
        return "Apartment: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, Окна выходят на {}.".format(self.living_rooms, self.square, self.combined_bath, self.floor, self.side)


class CountryHouseList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name


    def append(self, p_object):
        if type(p_object) == CountryHouse:
            super().append(p_object)
        else:
            raise TypeError('Invalid type {}'.format(type(p_object)))

    def total_square(self):
        res = 0
        for i in self:
            res += i.square
        return res


class ApartmentList(list):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        for i in iterable:
            if isinstance(i, Apartment):
                self.append(i)

    def floor_view(self, floors, directions):
        temp = list(filter(lambda x: x.floor in range(floors[0], floors[1] + 1) and x.side in directions, self))
        res = list()
        for i in temp:
            res.append("{}: {}".format(i.side, i.floor))
        print('\n'.join(res)) 