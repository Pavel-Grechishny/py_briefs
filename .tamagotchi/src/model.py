"""Model (MVC)."""

# ┌──────┐
# │ 2.25 │
# └──────┘

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Type, Iterable
from functools import cached_property
from pathlib import Path


# Переменные для аннотаций:
# Parameters: dict[Type, 'Parameter'] = {}
# Coefficients: dict[Type, dict[Type, float]] = {}



# DictOfRanges: dict[tuple[int, int], Any]
class DictOfRanges(dict):
    """Словарь диапазонов для возрастных периодов."""
    def __init__(self, mappable: dict):
        for key in mappable:
            if (
                not isinstance(key, tuple)
                or len(key) != 2
                or not isinstance(key[0], int)
                or not isinstance(key[1], int)
            ):
                raise ValueError('Invalid data type.')
        super().__init__(mappable)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            for left, right in self:
                if left <= key <= right:
                    return super().__getitem__((left, right))
        return super().__getitem__(key)
    

@dataclass
class KindParameter:
    """Обязательный видовой параметр питомца(существа)"""
    name: str
    initial: float
    min: float
    max: float


# observer
class CreatureParameter(ABC):
    """Параметр питомца(существа)"""
    name: str

    def __init__(
            self, 
            initial: float, 
            min: float, 
            max: float, 
            origin: 'Creature'
    ):
        self.__value = initial
        self._min = min
        self._max = max
        self.origin = origin

    @property
    def value(self) -> float:
        return self.__value

    @cached_property
    def range(self) -> tuple[float, float]:
        return (self._min, self._max)

    @value.setter
    def value(self, new_value: float) -> None: 
        if new_value <= self._min:
            self.__value = self._min
        elif self._max <= new_value:
            self.__value = self._max
        else:
            self.__value = new_value

    # @abstractmethod
    def update(self) -> None:
        pass


class Health(CreatureParameter):
    """Здоровье - параметр Tamagotchi."""
    name = 'Health'

    def update(self) -> None:
        """Обновление параметра."""

class Satiety(CreatureParameter):
    """Сытость - параметр Tamagotchi."""
    name = 'Satiety'

    def update(self) -> None:
        """Обновление параметра."""

class Fatigue(CreatureParameter):
    """Усталость - параметр Tamagotchi."""
    name = 'Fatigue'

    def update(self) -> None:
        """Обновление параметра."""

class Hygiene(CreatureParameter):
    """Чистота - параметр Tamagotchi."""
    name = 'Hygiene'

    def update(self) -> None:
        """Обновление параметра."""

class Mood(CreatureParameter):
    """Настроение - параметр Tamagotchi."""
    name = 'Mood'

    def update(self) -> None:
        """Обновление параметра."""

class Stamina(CreatureParameter):
    """Выносливость - параметр Tamagotchi."""
    name = 'Stamina'

    def update(self) -> None:
        """Обновление параметра."""

Parameters = Enum(
    'Parameters', 
    {
        cls.__name__: cls
        for cls in CreatureParameter.__subclasses__()
    }
)
# >>> Parameters
# <enum 'Parameters'>
# >>> list(Parameters)
# [<Parameters.Health: <class '__main__.Health'>>, 
#  <Parameters.Satiety: <class '__main__.Satiety'>>, 
#  <Parameters.Fatigue: <class '__main__.Fatigue'>>, 
#  <Parameters.Hygiene: <class '__main__.Hygiene'>>, 
#  <Parameters.Mood: <class '__main__.Mood'>>, 
#  <Parameters.Disease: <class '__main__.Disease'>>, 
#  <Parameters.Stamina: <class '__main__.Stamina'>>]
# >>>



class MaturePhase:
    """Возрастной период питомца (фаза зрелости)."""
        
    def __init__(
            self,
            days: int,
            *parameters: KindParameter
            # coeffs: dict = {}
    ):
        self.days = days
        self.parameters = parameters
        # self.coeffs = coeffs


# Реализовать хранение информации о виде в файле!!!
class Kind(DictOfRanges):
    """Описывает вид существа с характерными для него параметрами."""

    def __init__(
            self, 
            name: str, 
            *mature_phases: MaturePhase
    ):
        self.name: str = name
        left = 0
        phases = {}
        for phase in mature_phases:
            key_range = left, left + phase.days - 1
            phases[key_range] = phase
            left += phase.days
        super().__init__(phases)
        
# >>> cat = Kind(
# ...     'кот',
# ...     MaturePhase(5, None),
# ...     MaturePhase(15, None),
# ...     MaturePhase(35, None),
# ...     MaturePhase(55, None),
# ...     MaturePhase(75, None)
# ... )
# >>>
# >>> cat
# {
#     (0, 4): <__main__.MaturePhase object at 0x000002C810C07050>, 
#     (5, 19): <__main__.MaturePhase object at 0x000002C810F73290>, 
#     (20, 54): <__main__.MaturePhase object at 0x000002C810F73190>, 
#     (55, 109): <__main__.MaturePhase object at 0x000002C810F73250>, 
#     (110, 184): <__main__.MaturePhase object at 0x000002C810F730D0>
# }

# >>> cat[0]
# <__main__.MaturePhase object at 0x000001B034DB7050>
# >>> cat[-1]
# ...
# KeyError: -1
# >>> cat[10]
# <__main__.MaturePhase object at 0x000001B035123290>
# >>> cat[30]
# <__main__.MaturePhase object at 0x000001B035123190>
# >>> cat[40]
# <__main__.MaturePhase object at 0x000001B035123190>
# >>> cat[60]
# <__main__.MaturePhase object at 0x000001B035123250>
# >>> cat[160]
# <__main__.MaturePhase object at 0x000001B0351230D0>


class Creature:
    """Описывает питомца - игровое существо. Tamagotchi."""

    def __init__(
            self,
            kind: Kind,
            name: str,
    ):
        self.kind = kind
        self.name = name
        self.age: int = 0
        self.parameters: dict[Type, CreatureParameter] = {}
        for param in kind[0].parameters:
            cls = Parameters[param.name].value
            self.parameters[cls] = cls(
                param.initial,
                param.min,
                param.max,
                self
            )
        

    def update(self) -> None:
        """Обновление всех параметров Tamagotchi."""



cube = Kind(
    'Кубик', 
    MaturePhase(
        5, 
        KindParameter('Health', 100, 0, 100),
        KindParameter('Satiety', 100, 0, 100),
        KindParameter('Fatigue', 100, 0, 100),
        KindParameter('Hygiene', 100, 0, 100),
        KindParameter('Mood', 100, 0, 100),
        KindParameter('Stamina', 100, 0, 100)
    ),
    MaturePhase(
        20, 
        KindParameter('Health', 100, 0, 100),
        KindParameter('Satiety', 100, 0, 100),
        KindParameter('Fatigue', 100, 0, 100),
        KindParameter('Hygiene', 100, 0, 100),
        KindParameter('Mood', 100, 0, 100),
        KindParameter('Stamina', 100, 0, 100)
    ), 
    MaturePhase(
        50, 
        KindParameter('Health', 100, 0, 100),
        KindParameter('Satiety', 100, 0, 100),
        KindParameter('Fatigue', 100, 0, 100),
        KindParameter('Hygiene', 100, 0, 100),
        KindParameter('Mood', 100, 0, 100),
        KindParameter('Stamina', 100, 0, 100)
    )
)

yasha = Creature( 
    cube,
    'Yasha'
)

# >>> yasha
# <__main__.Creature object at 0x00000236DC9A0BD0>
# >>> for item in yasha.__dict__:
# ...     print(item)
# ...
# kind
# name
# age
# parameters
# >>>
# >>> yasha.kind
# {
#     (0, 4): <__main__.MaturePhase object at 0x00000236DC9A07D0>, 
#     (5, 24): <__main__.MaturePhase object at 0x00000236DC9A0990>, 
#     (25, 74): <__main__.MaturePhase object at 0x00000236DC9A0B50>
# }
# >>>
# >>> yasha.parameters
# {
#     <class '__main__.Health'>: <__main__.Health object at 0x00000236DC314390>, 
#     <class '__main__.Satiety'>: <__main__.Satiety object at 0x00000236DC3D5E50>, 
#     <class '__main__.Fatigue'>: <__main__.Fatigue object at 0x00000236DC1B4910>, 
#     <class '__main__.Hygiene'>: <__main__.Hygiene object at 0x00000236DC9A0B90>, 
#     <class '__main__.Mood'>: <__main__.Mood object at 0x00000236DC9A0C10>, 
#     <class '__main__.Stamina'>: <__main__.Stamina object at 0x00000236DC9A0C50>
# }
