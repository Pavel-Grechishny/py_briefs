from enum import Enum
from math import cos, sin
from typing import Self

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    
class BadPoint:
    
    def __init__(
            self,
            a: float,
            b: float,
            system: CoordinateSystem = CoordinateSystem.CARTESIAN
    ):

        if system is CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system is CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)



class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    @classmethod
    def cartesian(cls, x: float, y: float) -> Self:
        """Создает объект точки, заданной декартовыми координатами.
        
        :param x координата оси абсцисс
        :param y координата оси ординат
        """
        return cls(x, y)
        
    @classmethod
    def polar(cls, rho: float, phi: float) -> Self:
        """Создает объект точки, заданной полярными координатами.
        
        :param rho радиальная компонента
        :param phi азимут в радианах
        """
        x = rho * cos(phi)
        y = rho * sin(phi)
        return cls(x, y)
        
    def __repr__(self):
        return f'{self.__class__.__name__}: x={self.x}, y={self.y}'
        
        
# >>> p = Point(1, 2)
# >>> p
# Point: x=1, y=2
# >>> p1 = Point.cartesian(1, 2)
# >>> p1
# Point: x=1, y=2
# >>> p2 = Point.polar(1, 2)
# >>> p2
# Point: x=-0.4161468365471424, y=0.9092974268256817