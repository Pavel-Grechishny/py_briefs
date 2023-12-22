"""Model (MVC)."""

# ┌──────┐
# │ 2.25 │
# └──────┘

from abc import abstractmethod
from typing import Type, Iterable
from pathlib import Path

# ┌─────────────────────────────────────────────────────┐
# │ Переменные для аннотаций:                           │
# │ params: dict[Type, Parameter]                       │
# │ coeffs: dict[Type, dict[Type, float]]               │
# └─────────────────────────────────────────────────────┘

# ┌─────────────────────────────────────────────────────┐
# │ DictOfRanges: dict[tuple[int, int], Any]            │
# └─────────────────────────────────────────────────────┘
class DictOfRanges(dict):
    """Словарь диапазонов возрастных периодов."""
    def __getitem__():
        pass

# ┌─────────────────────────────────────────────────────┐
# │ Observer - наблюдатель                              │
# └─────────────────────────────────────────────────────┘
class Parameter:
    """Описывает параметр."""
    
    name = None
    
    def __init__(
            self,
            min: float,
            max: float,
            value: float,
        ):
        self.min = min
        self.max = max
        self.__value = value

    @abstractmethod
    def update(self) -> None:
        """Обновление параметра (связь параметров)."""
        pass

class MaturePhase:
    """Возрастной период питомца (фаза зрелости).
    
    :param days: количество возрастных дней в игровом периоде
    :param coeffs: матрица коэффициентов влияния параметров друг на друга
    """

    def __init__(
            self, 
            days: int, 
            params: dict[Type, Parameter], 
            coeffs: dict[Type, dict[Type, float]]
            # coefs[Satiety][Stamina]
        ):
        self.days = days
        self.params = params
        self.coeffs = coeffs


# ┌─────────────────────────────────────────────────────┐
# │ Реализовать хранение информации о виде в файле!!!   │
# └─────────────────────────────────────────────────────┘
class Kind(DictOfRanges):
    """Описывает вид существа с характерными для него параметрами."""

    def __init__(
            self, 
            name: str, 
            items: Iterable[MaturePhase]
        ):
        super().__init__(items)
        self.name_type: str = name
        self._path: Path = None
        self.image: Path = None


class Creature:
    """Описывает питомца - игровое существо. Tamagotchi."""

    def __init__(self, name: str):
        self.kind: Kind = None
        self.name: str = name
        self.age: int = 0
        self.params: dict[Type, Parameter]

    def update(self) -> None:
        """Обновление всех параметров Tamagotchi."""


# ┌─────────────────────────────────────────────────────┐
# │ Примерный список обязательных параметров Tamagotchi.│
# │ Health (здоровье)                                   │
# │ Satiety (сытость)                                   │
# │ Fatigue (усталость)                                 │
# │ Hygiene (гигиена, purity)                           │
# │ Mood (настроение)                                   │
# │ Disease (болезнь)                                   │
# │ Stamina (выносливость)                              │
# │ ...                                                 │
# └─────────────────────────────────────────────────────┘
class Health(Parameter):
    """Здоровье - параметр Tamagotchi."""
    name = 'Health'

    def update(self) -> None:
        """Обновление параметра."""

class Satiety(Parameter):
    """Сытость - параметр Tamagotchi."""
    name = 'Satiety'

    def update(self) -> None:
        """Обновление параметра."""

class Fatigue(Parameter):
    """Усталость - параметр Tamagotchi."""
    name = 'Fatigue'

    def update(self) -> None:
        """Обновление параметра."""

class Hygiene(Parameter):
    """Чистота - параметр Tamagotchi."""
    name = 'Hygiene'

    def update(self) -> None:
        """Обновление параметра."""

class Mood(Parameter):
    """Настроение - параметр Tamagotchi."""
    name = 'Mood'

    def update(self) -> None:
        """Обновление параметра."""

class Disease(Parameter):
    """Болезнь - параметр Tamagotchi."""
    name = 'Disease'

    def update(self) -> None:
        """Обновление параметра."""

class Stamina(Parameter):
    """Выносливость - параметр Tamagotchi."""
    name = 'Stamina'

    def update(self) -> None:
        """Обновление параметра."""


# ┌─────────────────────────────────────────────────────┐       
# │ Примерный список функций Tamagotchi                 │
# │ Накормить                                           │
# │ Напоить                                             │
# │ Уложить спать                                       │
# │ Гигиенические процедуры                             │
# │ Лечить, при необходимости                           │
# │ Играть                                              │
# │ ...                                                 │ 
# └─────────────────────────────────────────────────────┘

# alt196 ─
# alt179 │
# alt191 ┐
# alt192 └
# alt218 ┌
# alt217 ┘ 


# alt3 ♥
# alt4 ♦
# alt5 ♣
# alt6 ♠
# alt194 ┬
# alt195 ├
# alt197 ┼
# alt180 ┤
# alt193 ┴

# alt30 ▲
# alt31 ▼
# alt16 ►
# alt17 ◄

# alt176 ░
# alt177 ▒
# alt178 ▓

# alt219 █
# alt220 ▄
# alt221 ▌
# alt222 ▐
# alt223 ▀
    

