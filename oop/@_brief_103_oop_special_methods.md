### Специальные методы ###
>Специальные методы вызываются самим интерпретатором.

__new__
>Конструктор. Возвращает объект экземпляра класса.
Чаще всего применяется для создания экземпляра от базовых классов (int, str ...)

__del__ 
>Вызывается для удаления объекта из памяти и только в том случае когда количество ссылок на объект достигает '0'.
```python
class Test:
    def __del__(self):
        print('вызов __del__()')

# переменные ссылающися на Test
var = Test()
nums = [var, var]

# ссылок на объект Test равно '0'
print('первая операция')
var = 'abc'
print('вторая операция')
nums[0] = 'qwe'
```

__repr__
>Машиночитаемое строковое представление.

__str__
>Человекочитаемое строковое представление.

Если у объекта не был определен метод __str__, но был вызван,
то вместо него вызовется метод __repr__
```python
class Test:
    def __repr__(self):
        return 'repr tested'

class Test_2:
    def __repr__(self):
        return 'repr tested 2'
    def __str__(self):
        return 'str tested 2'

test = Test()
test_2 = Test_2()

test # -> repr tested
test_2 # -> repr tested 2

test_2.__str__() # -> 'str tested 2'
test_2.__repr__() # -> 'repr tested 2'

test.__repr__() # -> 'repr tested'
test.__str__() # -> 'repr tested'
```
Если для методов __str__ и __repr__ подразумевается одинаковое представление,
то мы определеяем одно и именно __repr__

__bytes__ - byte string
>Строка в которой можно явно указать (помощью 16-тиричного кода) байтовыую последовательность

__format__
>Можем определить собственные спецификации для форматирования
>Файл specials3.py

### 00_52 - перегрузка операторов ###
>Методы операций сравнения. Достаточно реализовать 3 метода\
object.__lt__(self, other)\
object.__le__(self, other)\
object.__eq__(self, other)\
object.__ne__(self, other)\
object.__gt__(self, other)\
object.__ge__(self, other)
>Файл specials4.py
```
python
from typing import Self

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def __eq__(self, other: Self):
        try:
            return {self.width, self.height} == {other.width, other.height}
        except AttributeError:
            try:
                return self.width == self.height == other.side
            except AttributeError:
                return False

rc1 = Rectangle(2, 3)
rc2 = Rectangle(2, 3)
rc3 = Rectangle(3, 2)
rc4 = Rectangle(4, 7)
rc5 = Rectangle(5, 5)

# до реализации методов сравнения
# >>> rc1 == rc2
# False
# >>>
# >>> id(rc1)
# 2111987977040
# >>> id(rc2)
# 2111987977168

# после реализации методов сравнения
# >>> rc1 == rc2
# True
# >>> rc1 == rc3
# True
# >>> rc1 == rc4
# False
# >>> rc1 == (2, 3)
# False

class Square:
    def __init__(self, side: float):
        self.side = side

sq1 = Square(5)

# >>> rc5 == sq1
# True
# >>> sq1 == rc5
# True
```

### 01_48 - __hash__() & __bool__() ###
>Объекты с одинаковыми хешам во время сравнения должны возвращать True.
>Любой объект может быть проверен на истинность. Так же собственный класс может быть проверен на истинность.
```python
bool(Test()) # -> Если метод не реализован в классе то всегда True
```
__bool__ связан с методом __len__(). Если метод __bool__ не определен, то вызывается метод __len__, если он определен.
И объект считается истинным, если резельтат не нулевой.
```python
class Test:
    def __len__(self):
        return 0

bool(Test()) # -> False
```

### 01_58 Доступ к атрибутам ###
> ... применять осторожно

### 02_04 - Эмуляция вызываемых объектов ###
> Файл specials5.py
> Реализуется за счет метода __call__ в нашем соственном классе
```python
class Computer:
    def __init__(self, cpu: str, ram: int):
        self.cpu = cpu
        self.ram = ram
    @staticmethod
    def start():
        print('Запуск компьютера')
    def __call__(self):
        return self.start()

pc = Computer('i7', 16)
pc() # -> Запуск компьютера
```

### 02_10 - Эмуляция контейнерных типов ###
__getitem__(self, key), __setitem__(self, key, value), __delitem__(self, key) - 
вызываются когда мы вычисляем обращение по индексу или ключу
> Файл specials6.py

### 02_40 - Эмуляция числовых типов ###
>У каждого из методов есть правосторонняя версия, которая вызывается в случае если у левого операнда не опрделен соответсвующий метод
> Файл specials7.py

