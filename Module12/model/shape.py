from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Abstract method not implemented")


@Shape.register
class Rectangle():
    def __init__(self, h, b):
        if h < 1 or b < 1:
            raise InvalidSideError
        if not isinstance(h, float) and not isinstance(h, int):
            raise InvalidSideError
        if not isinstance(b, float) and not isinstance(b, int):
            raise InvalidSideError
        self.height = h
        self.base = b

    def area(self):
        return self.height*self.base


class InvalidSideError(Exception):
    pass
