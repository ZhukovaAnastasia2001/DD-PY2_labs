import doctest


class Parallelepiped:
    def __init__(self, length: (int, float), width: (int, float), height: (int, float)):
        """"
        Создание и подготовка объекта "Прямоугольник" к работе

        :param length: Длина прямоугольника
        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника

        Примеры:
        >>> parallelepiped = Parallelepiped (30, 50, 20) #инициализация экземпляра класса
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Значение длины должно быть типа int или float")
        if length <=0:
            raise ValueError("Длина не может быть равной 0 или меньше")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Значение ширины должно быть типа int или float")
        if width <=0:
            raise ValueError("Ширина не может быть равной 0 или меньше")
        self.width = width


        if not isinstance(height, (int, float)):
            raise TypeError("Значение высоты должно быть типа int или float")
        if height <=0:
            raise ValueError("Высота не может быть равной 0 или меньше")
        self.height = height

    def perimeter(self):
        """
        Функция рассчитывает перимерт рёбер параллелепипеда
        :return: Периметр рёбер параллелепипеда

        Пример:
        >>> parallelepiped = Parallelepiped (30, 50, 20)
        >>> parallelepiped.perimeter ()
        """
        ...

    def area(self):
        """
        Функция рассчитывает площадь граней параллелепипеда
        :return: Площадь граней параллелепипеда

        Пример:
        >>> parallelepiped = Parallelepiped (30, 50, 20)
        >>> parallelepiped.area ()
        """
        ...

    def volume(self):
        """
        Функция рассчитывает объём параллелепипеда
        :return: Объём параллелепипеда

        Пример:
        >>> parallelepiped = Parallelepiped (30, 50, 20)
        >>> parallelepiped.volume ()
        """
        ...


class Muffin:
    def __init__(self, chocolate: int, eggs: int, sugar: int):
        """"
        Создание и подготовка объекта "Шоколадный маффин" к работе

        :param chocolate: Количество шоколада
        :param eggs: Количество яиц
        :param sugar: Количество сахара

        Примеры:
        >>> muffin =  Muffin (150, 2, 40) #инициализация экземпляра класса
        """

        if not isinstance(chocolate, int):
            raise TypeError("Количество шоколада должно быть типа int")
        if chocolate < 0:
            raise ValueError("Количество шоколада не может быть меньше 0")
        self.chocolate = chocolate

        if not isinstance(eggs, int):
            raise TypeError("Количество яиц должно быть типа int")
        if eggs < 0:
            raise ValueError("Количество яиц не может быть меньше 0")
        self.eggs = eggs

        if not isinstance(sugar, int):
            raise TypeError("Количество сахара должно быть типа int")
        if sugar < 0:
            raise ValueError("Количество сахара не может быть меньше 0")
        self.suger = sugar

    def buy_more_chocolate(self):
        """
        Функция проверяет достаточно ли шоколада для приготовления маффинов

        :return: Нужно ли купить ещё шоколада

        >>> muffin = Muffin(150, 2, 40)
        >>> muffin.buy_more_chocolate()
        """
        ...

    def buy_more_eggs(self):
        """
        Функция проверяет достаточно ли яиц для приготовления маффинов

        :return: Нужно ли купить ещё яиц

        >>> muffin = Muffin(150, 2, 40)
        >>> muffin.buy_more_eggs()
        """
        ...

    def buy_more_sugar(self):
        """
        Функция проверяет достаточно ли сахара для приготовления маффинов

        :return: Нужно ли купить ещё сахара

        >>> muffin = Muffin(150, 2, 40)
        >>> muffin.buy_more_sugar()
        """
        ...


class FireSafety:
    def __init__(self, apartment_area: (int, float), stairs: int, evacuation_path: (int, float)):
        """"
        Создание и подготовка объекта "Пожарная безопасность" к работе

        :param apartment_area: Общая жилая площадь на типовом этаже
        :param stairs: Количество лестниц
        :param evacuation_path: Длина эвакуационного пути от наиболее удалённой квартиры

        Примеры:
        >>> fire_safety = FireSafety (350, 1, 12) #инициализация экземпляра класса
        """

        if not isinstance(apartment_area, (int, float)):
            raise TypeError("Значение жилой площади должно принадлежать типам int или float")
        if apartment_area <= 0:
            raise ValueError("Жилая площадь не может быть равной 0 или меньше")
        self.apartment_area = apartment_area

        if not isinstance(stairs, int):
            raise TypeError("количество лестниц должно принадлежать типу int")
        if stairs < 1:
            raise ValueError("Количество лестниц не может быть меньше 1")
        self.stairs = stairs

        if not isinstance(evacuation_path, (int, float)):
            raise TypeError("Значение эвакауационного пути должно принадлежать типам int или float")
        if evacuation_path <= 0:
            raise ValueError("Эвакуационный путь не может быть равным 0 или меньше")
        self.evacuation_path = evacuation_path

    def floor_plan(self):
        """
        Функция проверяет соблюдаются ли требования ПБ, касательно длины эвакуационного пути
        :return: Необходимо ли пересмотреть планировку типового этажа

        Пример:
        >>> fire_safety = FireSafety(350, 1, 12)
        >>> fire_safety.floor_plan()
        """

    def add_stairs(self):
        """
        Функция проверяет достаточно ли лестниц исходя из жилой площади
        :return: Достаточно ли лестниц

        Пример:
        >>> fire_safety = FireSafety(350, 1, 12)
        >>> fire_safety.add_stairs()
        """

    if __name__ == "__main__":
        doctest.testmod()
# _
