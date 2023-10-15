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

test_2.__str__() # -> 'str tested 2'
test_2.__repr__() # -> 'repr tested 2'

test.__repr__() # -> 'repr tested'
test.__str__() # -> 'repr tested'
```


