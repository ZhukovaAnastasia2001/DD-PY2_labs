class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):

        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Название должно быть представлено строкой")

        if isinstance(author, str):
            self.author = author
        else:
            raise ValueError("Имя автора должно быть представлено строкой")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages: int):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            raise ValueError("Количество страниц должно быть целым положительным числом")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, duration:float):
        if isinstance(duration, float) and duration > 0:
            self._duration = duration
        else:
            raise ValueError("Значение длительности должно быть положительным числом")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._duration!r})"
#_
