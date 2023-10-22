## Наследование ##
Наследование - оно же обобщение. Идея заключается в том, что бы несколько отдельно взятых классов имели доступ к некоему одному набору атрибутов.
Это предполагается реализовать используя (выстраивание) иерархических зависимостей.
>Обобщение - вертикальная связь.
>Ассоциация - горизонтальная связь.
### Файл - inheritance1.py ###
```python
from pprint import pprint

class Parent:
    parent_attr = 'parent value'
    
class Child(Parent):
    child_attr = 'child value'
```
>Внутренне пространство имен родительского класса
```python
pprint(Parent.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#              'parent_attr': 'parent value',
#              '__dict__': <attribute '__dict__' of 'Parent' objects>,
#              '__weakref__': <attribute '__weakref__' of 'Parent' objects>,
#              '__doc__': None})
```
>Внутренне пространство имен дочернего класса
```python
pprint(Child.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#              'child_attr': 'child value',
#              '__doc__': None})
```
>Доступ к родительскому атрибуту возмржен за счет расширения области видимости.
```python
Child.parent_attr # -> 'parent value'
```
>Полностью расширенная область видимости дочернего класа(__dir__())
```python
dir(Child)
# [
#    '__class__',
#    ...
#    'child_attr',
#    'parent_arrt'
# ]
```

### 00_24 - Цепочки наследования ###
>Все классы, которые мы объявляем самостоятельно, восходят к корневому классу.
>Атрибут __mro__ (возвращает цепочку наследования (кортеж))
```python
Parent.__mro__ # -> (<class '__main__.Parent'>, <class 'object'>)
Child.__mro__ # -> (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)
```
**mro** - method resolution order (порядок разрешения методов)
Определяет в каком порядке будет расширяться пространство имен

**object** - родительский класс верхнего уровняю

### 00_38 - Одноименные атрибуты в наследовании ###
>Файл inheritance2.py
```python
class Parent:
    attr = 'parent value'

class Child(Parent):
    attr = 'child value'
```
>Одноименный атрибут в дочернем классе переопределится
```python
Parent.attr # -> 'parent value'
Child.attr # -> 'child value'
```

**Синонимы для классов**
|родительский|базовый|надкласс|superclass|
|дочерний|производный|подкласс|subclass|

### 00_44 - Эволюция. Файл - inheritance3.py ###

```python
class Proteus:
    @staticmethod
    def move():
        return 'движение'
    @staticmethod
    def eat():
        return 'питание'
    @staticmethod
    def reproduce():
        return 'размноежение'

class Fish(Proteus):
    @staticmethod
    def breath():
        return 'дыхание'

class Reptile(Fish):
    @staticmethod
    def hide():
        return 'скрытность'

class Bird(Reptile):
    @staticmethod
    def fly():
        return 'полёт'

class Mammal(Reptile):
    @staticmethod
    def care():
        return 'забота'

class Human(Mammal):
    @staticmethod
    def speak():
        return 'речь'

ivan = Human()
ivan.speak() # -> 'речь'
ivan.care() # -> 'забота'
ivan.fly() # -> AttributeError: 'Human' object has no attribute 'fly'
ivan.hide() # -> 'скрытность'
ivan.breath() # -> 'дыхание'
ivan.reproduce() # -> 'размноежение'
ivan.eat() # -> 'питание'
ivan.move() # -> 'движение'
```
**mro** - сработало у класса (у экземпляра - нет, только через класс)
```python
ivan.__mro__ # -> AttributeError: 'Human' object has no attribute '__mro__'
Human.__mro__ # -> (<class '__main__.Human'>, <class '__main__.Mammal'>, <class '__main__.Reptile'>, <class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)
ivan.__class__.__mro__ # -> (<class '__main__.Human'>, <class '__main__.Mammal'>, <class '__main__.Reptile'>, <class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)
```
### 01_03 - Person. Файл - inheritance4.py ###
```python
class Employee(Person):
    cls_attr = 'value'
    def __init__(self,
            last_name: str,
            first_name: str,
            patr_name: str,
            position: str,
            income: int
    ):
        super().__init__(last_name, first_name, patr_name)
        self.position = position
        self.income = income

anna = Person('Демидова', 'Анна', 'Олеговна')
anna.__dict__
# -> {'last_name': 'Демидова', 'first_name': 'Анна', 'patr_name': 'Олеговна'}

olga = Employee('Балашова', 'Ольга', 'Николаевна', 'Бухгалтер', 50000)
olga.__dict__
# -> {'last_name': 'Балашова', 'first_name': 'Ольга', 'patr_name': 'Николаевна', 'position': 'Бухгалтер', 'income': 50000}

anna.cls_attr # -> 'value'
olga.cls_attr # -> 'value'
```

### 01_54 - Плохое наследование. Файл inheritance5.py ###
```python
class Vehicle:
    wheels = 4
    def __init__(self, average_speed: int):
        self.speed = average_speed
    @staticmethod
    def move() -> str:
        return f'{self.__class__.__name__} moves on the ground with average speed of {self.speed} km/h'

class Bicycle(Vehicle):
    wheels = 2

class Car(Vehicle):
    pass

class Train(Vehicle):
    wheels = 16
    @staticmethod
    def move() -> str:
        return super().move().replace('on the ground', 'along railroads')

class Aircraft(Vehicle):
    wheels = 6
    def __init__(self, average_ground_speed: int, average_air_speed: int):
        self.ground_speed = average_ground_speed
        self.air_speed = average_air_speed
    @staticmethod
    def move() -> str:
        return f' On the ground {self.__class__.__name__} moves with average speed of {self.ground_speed} km/h while in air it flies with average speed of {self.air_speed} km/h'

sputnik = Bicycle(16)
volga = Car(60)
sapsan = Train(110)
ssj_100 = Aircraft(50, 500)

def sort_by_speed(*vehicles: Vehicle) -> list[Vehicle]:
    return sorted(vehicles, key=lambda v: v.speed)

sort_by_speed(sputnik, volga, sapsan, ssj_100)
# -> AttributeError: 'Aircraft' object has no attribute 'speed'

sort_by_speed(sputnik, volga, sapsan) 
# -> [<__main__.Bicycle object at 0x0000027C45DC4210>, <__main__.Car object at 0x0000027C45DC4610>, <__main__.Train object at 0x0000027C45DC4690>]
```

### 02_24


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 