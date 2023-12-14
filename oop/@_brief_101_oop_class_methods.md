# 00_01 - Вызов объекта класса

    Создание и вызов объекта класса обеспечивается метаклассами
    Метаклассы определяют поведение объектов классов
    
# Файл class3.py

    Тип объекта класса определяется еще одним объектом класса type
    type - это метакласс при помощи которого создается большинсктво объектов классов
    <!--class Person:
            def __init__(self, last_name: str, first_name: str):
                self.family = last_name
                self.name = first_name
                
        Person
        <class '__main__.Person'>
        
        type(Person)
        <class 'type'> 
    -->
    
    <!--ivan = Person('Fekistov', 'Inan')
        
        dir(ivan)
        [   
            '__class__',
            '__delattr__',
            '__dict__',
            '__dir__',
            '__doc__',
            '__eq__',
            '__format__',
            '__ge__',
            '__getattribute__',
            '__getstate__',
            '__gt__',
            '__hash__',
            '__init__',
            '__init_subclass__',
            '__le__',
            '__lt__',
            '__module__',
            '__ne__',
            '__new__',
            '__reduce__',
            '__reduce_ex__',
            '__repr__',
            '__setattr__',
            '__sizeof__',
            '__str__',
            '__subclasshook__',
            '__weakref__',
            'family',
            'name'
        ]
    -->
    
    В классе type определён метод __call__(cls, *args, **kwargs)
    В метод __call__(cls: -> объект класса, *args, **kwargs) -> 'instance'
    Метод __call__ -> возвращает экземпляр класса
    __new__() - статический метод (создает новый экземпляр от объекта класса)
    __init__() - связный метод (это не создающий метод, а инициализирующий, конфигурирующий метод)
    Общий вид создания экземпляра класса от объекта класса
    <!--def __call__(cls, *args, **kwargs) -> 'instanse':
        ...
        instance = cls.__new__(cls, *args, **kwargs)
        ...
        instance.__init__(*args, **kwargs)
        ...
        return instance
    -->
    
    __new__() -> метод конструктор
    __init__() -> метод конструктор
    
# 00_20 - Атрибуты класса, атрибуты экземпляра

# Файл - methods1.py

    <!--from pathlib import Path
        from sys import path

        class JournalFileInterface:
            default_path: Path = DIR / 'journal.log'
            def append(self, journal_entry: str, journal_path: str | Path = None) -> Path:
                if not journal_path:
                    journal_path = self.default_path
                with open(journal_path, 'a', encoding='utf-8') as fileout:
                    print(journal_entry, file=fileout)
            return journal_path

        jfi = JournalFileInterface()
        
        jfi.append('первая запись')
        WindowsPath('journal.log')
        
        jfi.append('вторая запись')
        WindowsPath('journal.log')
    -->
    
# 00_46 - is_absolute - метод

    Метод - is_absolute проверяет является ли путь абсолютным
    
    Если путь не абсолютный, то отстраиваем относительный путь от каталога со скриптом
    <!--if not journal_path.is_absolute:
            journal_path = DIR / journal_path
    -->
    
# 00_52 - Нужен ли экземпляр?

    <!--JournalFileInterface.append('так вызывать нельзя!')
        TypeError: JournalFileInterface.append() missing 1 required positional argument: 'journal_entry'

        JournalFileInterface.append(JournalFileInterface, 'так можно вызвать!')
        WindowsPath('journal.log')
    -->
    
# 00_55 - Классовые методы: @classmethod

    Для объявления классового метода используется встроенные декораторы
        @classmethod
    и в таком случае в первый позиционный аргумент будет передан не объект экземпляра (self)
        <!--def append(self, journal_entry: str, journal_path: str | Path = None) -> Path:-->
    а объект класса (cls)
        <!--def append(cls, journal_entry: str, journal_path: str | Path = None) -> Path:-->
    и тогда компоновка класса будет корректной и создавать экземпляр не нужно.
    и мы можем напряую от класса вызавать метод, где будет происходить подмена вызова.
        <!--JournalFileInterface.append('так можно вызвать!')-->
        <!--WindowsPath('journal.log')-->
    !!! Классовый метод можно вызывать и от экземпляра!!! 
        <!--jfi.append('вызов классового метода от экземпляра')-->
        <!--WindowsPath('journal.log')-->
        
# 01_06 - Статические методы: @staticmethod Файл - methods2.py

    @staticmethod - не осуществляется подмены вызова
    
    От экземпляра класса мы не можем напрямую вызвать метод объекта класса
    <!--class Informbureau:
            def warning():
                print('Граждане, будьте бдительны!')
            def emergency():
                print('ВНИМАНИЕ!')
    
        municipal = Informbureau()
        municipal.warning()
        TypeError: Informbureau.warning() takes 0 positional arguments but 1 was given

        municipal.__class__.warning()
        Граждане, будьте бдительны!
    -->
    
    У статического метода не производится подмены вызова.
    Объект класса и экземпляр ссылоются на один и тот же объект функцию
    и поэтому мы можем вызывать метод как от от объекта класса так и от экземпляра
    <!-- class Informbureau:
            @staticmethod
            def warning():
                print('Граждане, будьте бдительны!')
            @staticmethod
            def emergency():
                print('ВНИМАНИЕ!')
    
        Informbureau.warning
        <function Informbureau.warning at 0x00000236B1DC98A0>
        Informbureau.emergency
        <function Informbureau.emergency at 0x00000236B1DC9760>
        Informbureau.warning()
        Граждане, будьте бдительны!
        Informbureau.emergency()
        ВНИМАНИЕ!
    
        municipal = Informbureau()
        municipal.warning
        <function Informbureau.warning at 0x00000236B1DC98A0>
        municipal.emergency
        <function Informbureau.emergency at 0x00000236B1DC9760>
        municipal.warning()
        Граждане, будьте бдительны!
        municipal.emergency()
        ВНИМАНИЕ!
        
        Informbureau.warning is municipal.warning
        True
    -->
    
# 01_34 Класс Cat - файл methods3.py

    Класс Кошка
    Пременные могут называться одинаково, но при это быть в разных пространствах имен
    name - объекта класса : self.name - экземпляра класса
    
    <!--from random import choice, randrange as rr
        from typing import Self
    
        class Cat:
            names = ('Беляш','Черныш','Мурка','Барсик')
            colors = ('белый', 'черный', 'рыжий', 'полосатый')
            
            def __init__(self, name: str = None, color: str = None):
                if not name:
                    name = choice(self.names)
                self.name = name
                if not color:
                    color = choice(self.colors)
                self.color = color
            
            @staticmethod
            def meow() -> str:
                return 'мяу'
            
            def hungry(self) -> str:
                return '-'.join(self.meow() for _ in range(2, rr(3, 7)))
            
            @classmethod
            def reproduce(cls) -> list[Self]:
                return [cls() for _ in range(2, rr(3, 7))]
    
        yara = Cat('Яра', 'серо-полосатая')
        yara.meow()
        'мяу'
        
        yara.hungry()
        'мяу-мяу-мяу-мяу'
        yara.hungry()
        'мяу-мяу-мяу-мяу'
        yara.hungry()
        'мяу-мяу-мяу'
        yara.hungry()
        'мяу-мяу'
        
        kittens = yara.reproduce()    
        for kitty in kittens:
            print(f'{kitty.name}, {kitty.color}')
    
        Мурка, полосатый
        Барсик, белый
    -->
    
    Классовый метод может вызываться как от объекта класса, явно ничего не передавая,
    так и от экземпляра класса, явно ничего не передавая,
    при этом осуществляется подмена вызова с передачей в объект функции ссылки
    на объект класса
    <!--for kitty in Cat.reproduce():
            print(f'{kitty.name}, {kitty.color}')
 
        Черныш, белый
        Барсик, белый
        Барсик, рыжий
        Мурка, черный
    -->
    
# Машиночитаемое строковое представление - __repr__()

    По умолчанию
    <!--yara
        <__main__.Cat object at 0x000002065C53EB10>
    -->
    
    __repr__() - всегда должен возвращать строку
    не аннотируетя
    <!--
        def __repr__(self):
            return f'{self.name}: {self.color}'
            
        yara
        <Яра: серо-полосатая>  

        yara.__repr__()
        '<Яра: серо-полосатая>'
    -->
    
# Человекочитаемое строковое представление - __str__()
    
    <!--
        def __str__(self):
            return self.name
            
        print(yara)
        Яра

        yara.__str__()
        'Яра'
    -->
    
# Аннотации и документация

    self, cls - не аннотируются, остальные параметры - аннотируются
    специальные методы - не аннотируются, собственные методы - аннотируются
    методы (как и функции) должны иметь строку документации
    специальные методы - не документируются, собственные методы - документируются
    
# Файл - TextProcessor