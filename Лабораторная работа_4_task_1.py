class Cars:
    """ Базовый класс автомобили. """

    def __init__(self, price: float, engine: float, max_speed: int):
        """
        Создание и подготовка к работе объекта "Автомобили"
        :param price: цена в млн.руб.
        :param engine: объём двигателя в л
        :param max_speed: максимальная скорость в км/ч
        """
        self._price = price
        self._engine = engine
        self._max_speed = max_speed

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        if not isinstance(price, float):
            raise TypeError("Цена должна быть типа float")
        if price <= 0:
            raise ValueError("Цена должна иметь положительное значение")
        self._price = price

    @property
    def engine(self) -> float:
        return self._engine

    @engine.setter
    def engine(self, engine: float) -> None:
        if not isinstance(engine, float):
            raise TypeError("Значение объёма двигателя должно быть типа float")
        if engine <= 0:
            raise ValueError("Значение объёма двигателя должно быть положительным")
        self._engine = engine

    @property
    def max_speed(self) -> int:
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed: int) -> None:
        if not isinstance(max_speed, int):
            raise TypeError("Температура должна быть типа int")
        if max_speed <= 0:
            raise ValueError("Температура должна иметь положительное значение")
        self._max_speed = max_speed

    def __str__(self) -> str:
        """
        Функция, возврящающая строку
        :return: строка
        """
        return f"Цена автомобиля {self._price} млн.руб., объём двигателя: {self._engine}," \
               f" максимальная скорость: {self._max_speed} км/ч"

    def __repr__(self) -> str:
        """
        Функция, возвращающая валидную python строку
        :return: валидная строка
        """
        return f"{self.__class__.__name__}(price={self._price}, engine={self._engine!r}," \
               f" max_temp={self._max_speed})"

    def highest_speed(self, new_max_speed: int) -> None:
        """Функция, определяющая автомобиль с наибольшей максимальной скоростью"""
        if self._max_speed < new_max_speed:
            print("Этот автомобиль быстрее предыдущего")
        if self._max_speed >= new_max_speed:
            print("Этот автомобиль медленне предыдущего")


class BMW(Cars):
    """BMW. Дочерний класс"""

    def __init__(self, price: float, engine: float, max_speed: int, colour: str):
        """
        :param price: цена в млн.руб.
        :param engine: объём двигателя в л
        :param max_speed: максимальная скорость в км/ч
        :param colour: цвет кузова
        """
        super().__init__(price, engine, max_speed)
        self.colour = colour

    def __repr__(self) -> str:
        """
        Перегружаем метод __repr__, так как появился новый атрибут
        :return: валидная строка
        """
        return f"{self.__class__.__name__}(price={self._price}, engine={self._engine!r}," \
               f" max_speed={self._max_speed}, colour={self.colour!r})"

    class Audi(Cars):
        """Audi. Дочерний класс"""

        def __init__(self, price: float, engine: float, max_speed: int, interior_material: str):
            """
            :param price: цена в млн.руб.
            :param engine: объём двигателя в л
            :param max_speed: максимальная скорость в км/ч
            :param interior_material: материал салона
            """
            super().__init__(price, engine, max_speed)
            self.interior_material = interior_material

        def __repr__(self) -> str:
            """
            Перегружаем метод __repr__, так как появился новый атрибут
            :return: валидная строка
            """
            return f"{self.__class__.__name__}(price={self._price}, engine={self._engine!r}," \
                   f" max_speed={self._max_speed}, interior_material={self.interior_material!r})"


if __name__ == "__main__":
    Car_ = Cars(4.2, 2, 250)
    print(Car_)
    print(repr(Car_))
    BMW_1 = BMW(4.2, 2, 250, 'чёрный')
    BMW_2 = BMW(5.8, 3, 305, 'синий')
    print(BMW_1 == BMW_2)
    Car_.highest_speed(305)
#_
