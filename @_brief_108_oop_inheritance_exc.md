## Модель исключений ##

### 00_05 Exceptions_1.py ###

```python
ValueError # -> <class 'ValueError'>
ValueError.__mro__
# (
#    <class 'ValueError'>, 
#    <class 'Exception'>, 
#    <class 'BaseException'>, 
#    <class 'object'>
# )

ZeroDivisionError # -> <class 'ZeroDivisionError'>
ZeroDivisionError.__mro__
# (
#    <class 'ZeroDivisionError'>,
#    <class 'ArithmeticError'>,
#    <class 'Exception'>,
#    <class 'BaseException'>,
#    <class 'object'>
# )

Exception # -> <class 'Exception'>
Exception.__mro__
# (
#    <class 'Exception'>,
#    <class 'BaseException'>,
#    <class 'object'>
# )
```

**Наследование от Exception**

```python
class NotTextCharsError(Exception):
    pass

class UserName(str):
    def __new__(cls, value: str):
        instance = super().__new__(cls, value)
        if not instance.isalpha():
            raise NotTextCharsError
        return instance

login_1 = UserName('Abcdef')
login_1 # -> 'Abcdef'
type(login_1) # -> <class '__main__.UserName'>

login_2 = UserName('Abcdef1980') # -> NotTextCharsError
```

**Класс натурального числа**
```python
class NonNaturalNumberError(Exception):
    pass

class Natural(int):
    def __new__(cls, value: int):
        instance = super().__new__(cls, value)
        if instance <= 0:
            raise NonNaturalNumberError
        return instance

n1 = Natural(5)
n1 # -> 5

n2 = Natural(-5)
# ...
# NonNaturalNumberError
```

```python
buffer = '12 as (1,2) 0 -3 15'
natural_numbers = list()
for obj in buffer.split():
    try:
        natural_numbers.append(Natural(obj))
    except NonNaturalNumberError:
        natural_numbers.append(1)
    except (TypeError, ValueError):
        pass

natural_numbers
# -> [12, 12, 1, 1, 15]
```

```puthon
class NonNaturalNumberError(Exception):
    def __init__(self, class_):
        super().__init__(f'{class_.__name__!r} text Error')
```