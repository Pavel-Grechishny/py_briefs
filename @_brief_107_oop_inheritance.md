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

...


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 