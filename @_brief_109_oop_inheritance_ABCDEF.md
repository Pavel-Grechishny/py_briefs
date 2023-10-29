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
### 01_59
