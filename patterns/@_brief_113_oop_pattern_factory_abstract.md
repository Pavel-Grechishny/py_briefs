##Абстрактная фабрика##
> Порождающий - создание объекта

Возможность оперировать цепочками разных классов и их компоновать.
Выбираем из нескольких фабрик с помощью которых создаём конкретный экземпляр.

```python
"""Абстрактная фабрика"""

from abc import ABC, abstractmethod

class Drink(ABC):
    DRINK = True
    @abstractmethod
    def drink(self):
        pass

class Tea(Drink):
    def drink(self):
        print('Попить чай')

class Coffee(Drink):
    def drink(self):
        print('Попить кофе')

class DrinkFactory(ABC):
    @staticmethod
    @abstractmethod
    def prepare(amount: int) -> Drink:
        """Имитация сложного процесса настройки объекта.
        
        Обязательно возвращает экземпляр Drink.
        """
        pass

class TeaFactory(DrinkFactory):
    @staticmethod
    def prepare(amount: int) -> Tea:
        """Обязательно возвращает экземпляр Tea."""
        print('Кипятим воду')
        print(f'Кладём в воду {amount // 20} г чайных листьев')
        print(f'Наливаем в чашку {amount} мл кипятка')
        return Tea()
  
class CoffeeFactory(DrinkFactory):
    @staticmethod
    def prepare(amount: int) -> Coffee:
        """Обязательно возвращает экземпляр Coffee."""
        print(f'Кладём в турку {amount // 20} ч.л. молотого кофе')
        print(f'Наливаем в турку {amount} мл холодной воды')
        print(f'Держим кофе на слабом огне до закипания')
        return Coffee()

# Управляющий код верхнего уровня
def make_drink(kind: str) -> Drink:
    """Возвращает определенное количество нужного напитка"""
    if kind.lower() in ('tea', 'чай'):
        return TeaFactory.prepare(200)
    elif kind.lower() in ('coffee', 'кофе'):
        return CoffeeFactory.prepare(50)
    else:
        return None

# # тест

# what_do_you_want = input('Чай / Кофе ? > ')
# hot_drink = make_drink(what_do_you_want)
# hot_drink.drink()

# # Чай / Кофе ? > Чай
# # Кипятим воду
# # Кладём в воду 10 г чайных листьев
# # Наливаем в чашку 200 мл кипятка
# # Попить чай

# # Чай / Кофе ? > Кофе
# # Кладём в турку 2 ч.л. молотого кофе
# # Наливаем в турку 50 мл холодной воды
# # Держим кофе на слабом огне до закипания
# # Попить кофе
```

