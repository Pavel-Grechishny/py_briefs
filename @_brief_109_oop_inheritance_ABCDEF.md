## Множественное наследование ##

### Файл multi_inheritance_1.py ###
**Разница в порядке указания классов наследования**
```python
class A:
    attr = 'A'

class B:
    attr = 'B'

class C(A, B):
    pass

class D(B, A):
    pass

class E(D):
    pass
A.__mro__
# (<class '__main__.A'>, <class 'object'>)

B.__mro__
# (<class '__main__.B'>, <class 'object'>)

C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

E.__mro__
# (<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```
**Невозможность наследования**
```python
class F(C, D):
    pass
    
# ...
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
```
**Противорецие цепочек**
>от class C - class '__main__.A', class '__main__.B'

>от class D - class '__main__.B', class '__main__.A'

### Файл multi_inheritance_2.py ###
```python
class A:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор A')
        self.attr = 'атрибут A'

class B:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор B')
        self.attr = 'атрибут B'

class C(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор C')
        super().__init__()

C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
c = C()
# экземпляр C: конструктор C -> вызов собственного конструктора
# экземпляр C: конструктор A -> вызов конструктора родительского класса
c.attr
# 'атрибут A'
```
### 01_59 - Функция super() ###
>Функция super() начинает поиск, начина со следующего по цепочке __mro__ класса при создании экземпляра класса
```python
class A:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор A')
        self.attr = 'атрибут A'

class B:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор B')
        self.attr = 'атрибут B'

class C(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор C')
        super().__init__()

class D(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор D')
        super(A, self).__init__()

D.__mro__
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

d = D()
# экземпляр D: конструктор D -> вызов собственного конструктора
# экземпляр D: конструктор B -> вызов конструктора класса следующего после A

d.attr
# 'атрибут B'
```
>продолжение (!C и D - имеют одинаковые цепочки __mro__)
```python
class E:
    pass

class F(E, C, D):
    pass

F.__mro__
# <class '__main__.F'>,
# <class '__main__.E'>,
# <class '__main__.C'>,
# <class '__main__.D'>,
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class 'object'>

f.attr
# 'атрибут B'
```
>продолжение (создаем экземпляр F)
```python
f = F()
# экземпляр F: конструктор C
# экземпляр F: конструктор D
# экземпляр F: конструктор B
```

>при создании экземпляра f = F():
1. F - не имеет конструктора и его мы пропускаем
2. E - не имеет конструктора и его мы пропускаем
3. C - конструктор есть и мы его вызываем
4. C - вызывает родительский конструктор 
5. С - для него родительским конструктором является A
6. C - но для коструктора C вызван был конструктор D
7. Потому, что когда мы вызываем контруктор C, то мы его вызываем для экземпляра класса F и цепочка __mro__ будет взята из экземпляра класса f
8. А для экземпляра класса f - по цепочке __mro__ для класса C, **как бы** родительским, является класс D
9. Поэтому вызов функции super в конструкторе класса C для экземпляра f приводит к вызову конструктора D (следующего) 
10. А конструктор D - уже вызывает конструктор B
11. В итоге f.attr -> 'атрибут B'  

### 02_29 - Классы примеси ###
**Примесь - класс который реалицует некоторую функциональность и эту функц-сть мы хотим "подмешивать" к разным классам (из разных цепочек наследования)**
```python
from collections.abc import Iterable

class Printable:
    def print(self) -> None:
        print('\n'.join(
            f'{attr}: {value!r}'
            for attr, value in self.__dict__.items()))

class Person:
    def __init__(self, l_name: str, f_name: str, p_name: str):
        self.l_name = l_name
        self.f_name = f_name
        self.p_name = p_name
    def __repr__(self):
        return f'{self.f_name} {self.p_name} {self.l_name}'

class Student(Person, Printable):
    def __init__(self, l_name: str, f_name: str, p_name: str, year: int):
        super().__init__(l_name, f_name, p_name)
        self.year = year

class CatalogueCard:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

class BookCard(CatalogueCard):
    def __init__(self, title: str, year: int, author: Person, *authors: Person):
        super().__init__(title, year)
        self.authors: tuple[Person, ...] = author, *authors

class CompendiumCard(CatalogueCard, dict, Printable):
    def __init__(self, title: str, year: int, articles: dict[str, Iterable[Person]]):
        super().__init__(title, year)
        super(CatalogueCard, self).__init__(articles)

class CompendiumCard(CatalogueCard, dict, Printable):
    def __init__(self, title: str, year: int, articles: dict[str, Iterable[Person]]):
        super(CompendiumCard, self).__init__(title, year)
        super(CatalogueCard, self).__init__(articles)

CompendiumCard.__mro__
# <class '__main__.CompendiumCard'>, 
# <class '__main__.CatalogueCard'>, 
# <class 'dict'>, 
# <class '__main__.Printable'>, 
# <class 'object'>

vu_ivanov = Person('Иванов', 'Владимир', 'Юрьевич')
en_zakhavrov = Person('Захаров', 'Евгений', 'Николаевич')
art_1 = 'Применение теории управления конечными автоматами в производстве РФП'
fti_2020 = CompendiumCard('Летняя конференция ФТИ - 2020', 2020, {art_1: [vu_ivanov, en_zakhavrov]})

fti_2020
# {'Применение теории управления конечными автоматами в производстве РФП': [Владимир Юрьевич Иванов, Евгений николаевич Захаров]}

fti_2020.print()
# title: 'Летняя конференция ФТИ - 2020'
# year: 2020
```