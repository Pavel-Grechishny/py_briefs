# Инкапсуляция #

## 00_01 - Области видимости ##

    В ООП - изучется несколько областей видимости к атрибутам некоторого объекта.
    У каждого объекта есть обязательно доступ к атрибутам, но внутреннего пространства имен может не быть.
    
Инкапсуляция решает:
1 - часть - это ограничения уровня доступа к атрибутам напрямую
2 - часть - это контролируемое управление атрибутами

    
Например у int нет внутреннего пространства имен, но есть доступ к атрибутам:

    >>> a = 5
    >>> type(a)     -> <class 'int'>
    >>> a.__class__ -> <class 'int'>
    >>> a.__dict__  -> AttributeError: 'int' object has no attribute '__dict__'. Did you mean: '__dir__'?
    >>> 
    >>> a.__dir__()
    [
        '__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__',
        '__add__', '__radd__', '__sub__', '__rsub__', '__mul__', '__rmul__', '__mod__', '__rmod__', '__divmod__', 
        '__rdivmod__', '__pow__', '__rpow__', '__neg__', '__pos__', '__abs__', '__bool__', '__invert__', '__lshift__',
        '__rlshift__', '__rshift__', '__rrshift__', '__and__', '__rand__', '__xor__', '__rxor__', '__or__', '__ror__', 
        '__int__', '__float__', '__floordiv__', '__rfloordiv__', '__truediv__', '__rtruediv__', '__index__', 'conjugate',
        'bit_length', 'bit_count', 'to_bytes', 'from_bytes', 'as_integer_ratio', '__trunc__', '__floor__', '__ceil__',
        '__round__', '__getnewargs__', '__format__', '__sizeof__', 'real', 'imag', 'numerator', 'denominator', '__doc__',
        '__str__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__reduce__', '__getstate__',
        '__subclasshook__', '__init_subclass__', '__dir__', '__class__'
    ]

    
Инкапсуляция - это:\
Определяются различные уровни видимости, различные уровни доступа для разных атрибутов объектов
Выделяют 3 уровня доступа: (!!! на теоретическом уровне)
1. public    - публичный (доступ и на чтение и на запись из внешнего пространства имен)
2. private   - частный (доступ только на чтение из внешнего пространства имен)
3. protected - защищенный (нет доступа ни на чтение ни на запись из внешнего пространства имен)
    
## Файл - incapsulation ##

Проблема в том, при измении стороны, площадь не изменилась.
>!Рассогласование!
```python
    class Square:
        def __init__(self, side: int):
            self.side = side
            self.area = side**2
        
    sq = Square(5)
    sq.side -> 5
    sq.area -> 25
    
    sq.side = 10
    sq.side -> 10
    sq.area -> 25
```  

Проблема в том, что мы должны максимально острожно изменять атрибуты
>Перекрытие доступа к атрибутам!
>Нужен контролируемый доступ!
    
```python
    class User:
        def __init__(self, login: str, email: str, password: str):
            # публичные атрибуты
            self.login = login
            self.email = email
            self.password = hash(password)
    
    ivan = User('ivan', 'ivan@mail.ru', 'qwerty')
    ivan.login    # 'ivan'
    ivan.email    # 'ivan@mail.ru'
    ivan.password # 196247794774218261
```
    
## 00_28 Сеттеры & Геттеры & Леттеры - 00_55 ##

Методы при помощи которых мы контролируемо (управляем значениями атрибутов):
1. с одной стороны предоставляем значение какого либо атрибута      - Геттеры
2. с другой стороны изменяем значение какого либо атрибута          - Сеттеры
3. для удаления значения атрибута из пространства имен используются - Леттеры
    
## 00_32 Подход Python к инкапсуляции ##

>В Python инкапсуляция реализована не полностью!\
Ограничение уровня доступа в Python напрямую невозможно!\
Любой объект имет доступ к любому объекту!
    
Иммитация уровня доступа в Python:
1. public    -   attr (без подчеркивания)
2. private   -  _attr (одно подчеркивание)
3. protected - __attr (два подчеркивания)
    
    
Работает? Да, но не совсем...
```python
    class User:
        def __init__(self, login: str, email: str, password: str):
            
            # публичный public
            self.login = login
            # частный private
            self._email = email
            # защищенный protected
            self.__password = hash(password)
    
    user = User('user', 'mail', 'pass')
    user.login      # 'user'
    user._email     # 'mail'
    user.__password # AttributeError: 'User' object has no attribute '__password'
```
    
>...во внутреннем пространстве имён увидим... _User__password\
... _User__password - _ИмяКласса__атрибут
```python
    user.__dict__ 
    # {'login': 'user', '_email': 'mail', '_User__password': 2897226804880369300}
```
Если обратиться к нему так как он записан, то получим доступ к атрибуту\
>Потому, что работает механизм - подмены имён - name mandling, для защищенных атрибутов!
```python
    user._User__password
    # 2897226804880369300
```
    
>Проверяем изменение атрибутов. Ограничить доступ не можем.
```python
    user.login = 'bugaga'
    user._email = 'figtebe'
    user._User__password = 'ugadaika'
    user.__dict__
    # {'login': 'bugaga', '_email': 'figtebe', '_User__password': 'ugadaika'}
```
    
## 00_50 - Использование меток '_' & '__'. Файл - incapsulation2.py ##

Для командной работы (разработки)\
Для интегрированной среды разработки\
Для динамического работы с пространствами имен
    
    
## 00_55 - Сеттеры & Геттеры ##

Решение проблемы рассогласования при помощи сеттеров
```python
    class Square:
        def __init__(self, side: float):
            self.side = side
            self.area = side**2
    
        # классический геттер
        def get_side(self) -> float:
            return self.side
    
        # классический сеттер
        def set_side(self, new_side: float) -> None:
            self.side = new_side
            self.area = new_side**2

        # классический геттер
        def get_area(self) -> float:
            return self.area

        # классический сеттер
        def set_area(self, new_area: float) -> None:
            self.side = new_area**0.5
            self.area = new_area
```
>Возникает проблема рассогласования    
```python
    sq = Square(3)
    sq.side # 3
    sq.area # 9
    sq.side = 10
        
    #Проблема рассогласования
    sq.side # 10
    sq.area # 9
```
        
>Решение проблемы рассогласования при помощи сеттера
```python
    sq.set_side(12)
    sq.side # 12
    sq.area # 144
    sq.set_area(225)
    sq.area # 225
    sq.side # 15.0
```
    
## 01_12 - Динамический доступ на чтение и запись (встроенные getattr() & setattr()) ##
 
Динамический доступ на чтение - getattr()
```python
    for attr_name, attr_value in user.__dict__.items():
        if not attr_name.startswith(f'_{user.__class__.__name__}'):
            print(f'{attr_name}: {getattr(user, attr_name)!r}')
    # login: 'bugaga'
    # _email: 'figtebe'
```
    
Динамический доступ на запись - setattr()
```python
    for attr_name in user.__dict__:
        if not attr_name.startswith('_'):
            setattr(user, attr_name, 'новое значение')
            print(f'{attr_name}: {getattr(user, attr_name)!r}')
    # login: 'новое значение'

    for attr_name, attr_value in user.__dict__.items():
        if attr_name.startswith(f'_{user.__class__.__name__}'):
            setattr(user, attr_name, 'новое значение')
            print(f'{attr_name}: {getattr(user, attr_name)!r}') 
    #_User__password: 'новое значение'
```
    
## 01_43 - Защищенные атрибуты в классе ##

Защищенные атрибуты
>тут side - объект метода
```python    
    class Square:
        def __init__(self, side: float):
            self.__side = side
            self.__area = side**2
            
        def side(self) -> float:
            return self.__side
    
    sq = Square(10)
    sq.side # <bound method Square.side of <__main__.Square object at 0x00000238FADF4350>>
    sq.side() # 10
``` 
    
Декорируем при помощи @property
>тут side - значение
```python
    class Square:
        def __init__(self, side: float):
            self.__side = side
            self.__area = side**2
            
    # это геттер
        @property
        def side(self) -> float:
            return self.__side
    
    sq = Square(10)
    sq.side # 10
```
    
Декоратор @protected работает таким образом, что при обращении к декорируемому методу
как к атрибуту, метод вызывается и возвращает значение, 
которое должен вернуть вызванный метод без декоратора
```python
    # Без использования декоратора
    sq.side   # <bound method Square.side of <__main__.Square object at 0x00000238FADF4350>>
    sq.side() # 10

    # с использованием декоратора
    # @property
    sq.side # 10 
```
>В итоге получаем возможность работь с методом, как с атрибутом!
>За счет @property получаем контролируемый доступ управления атрибутом!

Для задания сеттера необходимо написать ОДНОИМЕННЫЙ метод с ОДНИМ аргументом
```python
    @property
    def side(self) -> float:
        ...
    
    @side.setter
    def side(self, new_side: float) -> None:
        ...
```
    
>Пример
```python
    class Square:
        def __init__(self, side: float):
            self.__side = side
            self.__area = side**2

        #геттер
        @property
        def side(self) -> float:
            return self.__side

        # сеттер
        @side.setter
        def side(self, new_side: float) -> None:
            self.__side = new_side
            self.__area = new_side**2
            
    sq = Square(4.44)
    sq.side # 4.44 -> геттер - получаем атрибут __side при помощи @property def side()
    sq.side = 6.02  # сеттор - устанавливаем    __side при помощи @side.setter def side()
    sq.side # 6.02 -> геттер - получаем атрибут __side при помощи @property def side()
```
**Объявить сеттер @side.setter без геттара @property НЕЛЬЗЯ!**
    
## 02_04 - Файл - property2.py ##

    ...
    
    
    
    