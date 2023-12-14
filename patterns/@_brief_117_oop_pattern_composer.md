## Компоновщик ##

> Структурный - взаимосвязь сущностей

Связь между группами


```python
"""Компоновщик"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class VectorGraphicObject(ABC):
    @abstractmethod
    def render(self):
        pass


@dataclass
class Line(VectorGraphicObject):
    name: str
    length: float
    
    def render(self):
        print(f'{self.name}: {self.length}')


@dataclass
class Text(VectorGraphicObject):
    name: str
    text: str
    
    def render(self):
        print(self.text)


class Group(VectorGraphicObject):
    def __init__(self, name: str):
        self.name = name
        self.__elements: list[VectorGraphicObject] = []
        
    def add_elements(args: VectorGraphicObject):
        self.__elements.extend(args)
        
    def render(self):
        for elem in self.__elements:
            elem.render()


# >>> ab = Line('AB', 3)
# >>> bc = Line('BC', 3)
# >>> ca = Line('CA', 3)
# >>>
# >>> formula = Text('perimetr', 'P = AB + BC + CA')
# >>>
# >>> ab.render()
# AB: 3
# >>>
# >>> formula.render()
# P = AB + BC + CA
```