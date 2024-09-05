from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        self.__sides = sides if len(sides)==self.sides_count else [1]*self.sides_count


    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return (0<=r<=255 and 0<=g<=255 and 0<=b<=255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self,*sides):
        flag = True
        for side in sides:
            if side<=0 or not isinstance(side,int):
                flag = False
        return flag and len(sides)==self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides)==self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = self.get_radius(circumference)

    @staticmethod
    def get_radius(circumference):
        return circumference/(2*pi)

    def get_square(self):
        return pi*(self.__radius)**2


class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        a, b, c = self.__sides
        p=sum(self._Figure__sides)/2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        sides = [side]*12
        super().__init__(color, *sides)

    def get_volume(self):
        return self._Figure__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216