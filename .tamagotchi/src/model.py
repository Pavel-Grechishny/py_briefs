"""Model (MVC)."""


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
    
    def __init__(
            self,
            name: str, 
            min: float,
            max: float,
            value: float,
        ):
        self.name = name
        self.min = min
        self.max = max
        self.__value = value


class MaturePhase:
    """Возрастной период питомца (фаза зрелости).
    
    :param days: количество возрастных дней в иговом периоде
    """

    def __init__(
            self, 
            days: int, 
            params: dict[Type, Parameter], 
            coeffs: dict[Type, dict[Type, float]]
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
        """Обновление параметров состояния экземпляра."""


# ┌─────────────────────────────────────────────────────┐
# │ Примерный список обязательных параметров Tamagotchi.│
# │ Health (здоровье)                                   │
# │ Satiety (сытость)                                   │
# │ Fatigue (усталость)                                 │
# │ Hygiene (гигиена, purity)                           │
# │ Mood (настроение)                                   │
# │ Disease (болезнь)                                   │
# │ ...                                                 │
# └─────────────────────────────────────────────────────┘
class Health(Parameter):
    """Здоровье - параметр Tamagotchi."""

class Satiety(Parameter):
    """Сытость - параметр Tamagotchi."""

class Fatigue(Parameter):
    """Усталость - параметр Tamagotchi."""

class Hygiene(Parameter):
    """Чистота - параметр Tamagotchi."""

class Mood(Parameter):
    """Настроение - параметр Tamagotchi."""

class Disease(Parameter):
    """Болезнь - параметр Tamagotchi."""


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