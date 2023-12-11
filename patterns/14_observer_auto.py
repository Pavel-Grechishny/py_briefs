"""Демонстратор наблюдателя: автоматическая подписка и отмена подписки."""

from abc import ABC


class Observers(list):
    """Вызываемый список наблюдателей."""
    def __call__(self, *args, **kwargs):
        for observer in self:
            # Вызов наблюдателя
            observer(*args, **kwargs)


class Observable(ABC):
    """Интерфейс наблюдаемого объекта."""
    def __init__(self):
        # Список наблюдателей
        self.properties_changed = Observers()


class Person(Observable):
    """Наблюдаемый объект."""
    def __init__(self):
        super().__init__()
        # Наблюдаемый атрибут
        self.__age: int = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        """Оповещает наблюдателей при изменении значения атрибута."""
        if self.__age == value:
            return
        self.__age = value
        self.properties_changed('age', value)


class TrafficAuthority:
    """Инфраструктура наблюдателя."""
    def __init__(self, person: Person):
        self.person = person
        # Автоматическая подписка.
        self.person.properties_changed.append(self.age_changed)

    def age_changed(self, prop_name: str, prop_value: int):
        """Метод наблюдатель."""
        if prop_name == 'age':
            if prop_value < 18:
                print('Вам запрещено управлять автомобилем.')
            else:
                print('Вам разрешено управлять автомобилем.')
                # Автоматическая отмена подписки
                self.person.properties_changed.remove(self.age_changed)


# >>> dima = Person()
# >>> gibdd = TrafficAuthority(dima)
# >>> for age in range(12, 30):
# ...     print(f'{age = }')
# ...     # генерация события
# ...     dima.age = age
# ...
# age = 12
# Вам запрещено управлять автомобилем.
# age = 13
# Вам запрещено управлять автомобилем.
# age = 14
# Вам запрещено управлять автомобилем.
# age = 15
# Вам запрещено управлять автомобилем.
# age = 16
# Вам запрещено управлять автомобилем.
# age = 17
# Вам запрещено управлять автомобилем.
# age = 18
# Вам разрешено управлять автомобилем.
# age = 19
# age = 20
# age = 21
# age = 22
# age = 23
# age = 24
# age = 25
# age = 26
# age = 27
# age = 28
# age = 29