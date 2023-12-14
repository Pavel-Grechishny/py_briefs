## Композиция и агрегация ##

> Все сущности, которые мы создаем, могут быть связаны 2-мя видами связи\

В ООП эти звязи называются 
1. Ассоциация
2. Обобщение

Ассоциация - это вид связи с помощью которого мы показываем включение объектов друг в друга. 
Использование различными объектами (сущностями) друг друга, т.е. мы ассоциируем один объект с другим говоря,
что они используются совместно.

>Композиция и агрегация - это различные проявления ассоциации

### 00_03 - Агрегация. Файл - agregation1.py ###
> Экземпляры классов, которые мы создаем самостоятельно, передаются по ссылке
```python
class A:
    def __init__(self):
        self.attr = 'арибут класса A'

class B:
    def __init__(self, assotiated_object: A):
        self.assotiated = assotiated_object

a = A() # -> ассоциируемый класс
b = B(a)

a # -> <__main__.A object at 0x000002E1AF350910>
a.attr # -> 'арибут класса A'

b # -> <__main__.B object at 0x000002E1AF6BB750>
b.assotiated # -> <__main__.A object at 0x000002E1AF350910>
```
> Если в атрибуте **assotiated** записана ссылка на объект **а**, то мы можем обратиться его атрибуту **attr**
```python
b.assotiated.attr # -> 'арибут класса A'
```
Поэтому в этом случае, имея доступ к объекту **b** мы можем использовать атрибут объекта **a**

** Агрегация и композиция отличаются тем, что в агрегации ассоциируемый класс являются независимыми и может использоваться отдельно **

### 00_15 - Композиция. Файл - composition1.py ###
```python
class Person:
    class Sex:
        M = 'мужской'
        F = 'женский'
    def __init__(self, family: str, name: str, sex: str):
        self.last_name = family
        self.first_name = name
        self.sex = sex

ivan = Person('Денисов', 'Иван', Person.Sex.M)
liza = Person('Макарова', 'Елизавета', Person.Sex.F)
```
>Одним из атрибутов класса Person, стал объект класса Sex\
```python
Person # -> <class '__main__.Person'>
print(*Person.__dict__.items(), sep='\n')
# -> ('__module__', '__main__')
# -> ('Sex', <class '__main__.Person.Sex'>)
# -> ('__init__', <function Person.__init__ at 0x000002E1AF6C3560>)
# -> ('__dict__', <attribute '__dict__' of 'Person' objects>)
# -> ('__weakref__', <attribute '__weakref__' of 'Person' objects>)
# -> ('__doc__', None)

Person.Sex.M # -> 'мужской'
Person.Sex.F # -> 'женский'

ivan.sex # -> 'мужской'
liza.sex # -> 'женский'
```
**Ключевое отличие - объявляя класс в пространстве имен другого класса, мы объяеляем этот класс ЗАВИСИМЫМ!!!**
Мы утверждаем, что эти классы могут использоваться только совместно. Класс **Sex** имеет мало значения за пределами класса **Person**.

## 00_31 - Агрегация(пример). Файл - aregation2.py ##
> Класс продукт\
```python
from datetime import date, datetime as dt, timedelta as td
class Product:
    date_format: str = '%d.%m.%Y'
    def __init__(
            self,
            name: str,
            expiration: int,
            produced: date | str = date.today()):
        self.name = name
        if isinstance(produced, str):
            produced = dt.strptime(produced, self.date_format).date()
        self.produced: date = produced
        self.expiration: date = produced + td(days=expiration)
    def is_expired(self) -> bool:
        return date.today() > self.expiration
    def __repr__(self):
        return f'<{self.name}: {self.produced:{self.date_format}}...{self.expiration:{self.date_format}}>'

prods = (
    Product('молоко', 7, '15.10.2023'),
    Product('хлеб', 6, '15.10.2023'),
    Product('морковь', 5, '5.10.2023'),
    Product('шоколад', 120, '5.10.2021'))

print(*prods, sep='\n')
# -> <молоко: 15.10.2023...22.10.2023>
# -> <хлеб: 15.10.2023...21.10.2023>
# -> <морковь: 05.10.2023...10.10.2023>
# -> <шоколад: 05.10.2021...02.02.2022>

for pr in prods:
    print(f'{pr.name}: {pr.is_expired()}')

# -> молоко: False
# -> хлеб: False
# -> морковь: True
# -> шоколад: True
```
> Класс холодильник\
```python
class Fridge:
    def __init__(self, *products: Product):
        self.__camera: list[Product] = list(products)
    def __iter__(self):
        return iter(self.__camera)
    def __len__(self):
        return len(self.__camera)
    def __getitem__(self, index: int) -> str:
        return self.__camera[index]
    def __delitem__(self, index: int):
        print('Вызов __delitem__()')
        del self.__camera[index]
    def put(self, product: str):
        if isinstance(product, str):
            self.__camera.append(product)
    def __repr__(self):
        products = '\n'.join(repr(pr) for pr in self.__camera)
        return '\n'.join((
            'ХОЛОДИЛЬНИК',
            '-----------',
            products
        ))
```
> Тесты холодильника и продуктов
```python
minsk = Fridge(*prods)

minsk
# -> ХОЛОДИЛЬНИК
# -> -----------
# -> <молоко: 15.10.2023...22.10.2023>
# -> <хлеб: 15.10.2023...21.10.2023>
# -> <морковь: 05.10.2023...10.10.2023>
# -> <шоколад: 05.10.2021...02.02.2022>
```

>Добавляем метод clear_expired()
```python
from itertools import filterfalse


def clear_expired(self):
    self.__camera = list(filterfalse(
        lambda pr: pr.is_expired(),
        self.__camera
    ))

minsk.clear_expired()    
minsk
# -> ХОЛОДИЛЬНИК
# -> -----------
# -> <молоко: 15.10.2023...22.10.2023>
# -> <хлеб: 15.10.2023...21.10.2023>
```
    
    