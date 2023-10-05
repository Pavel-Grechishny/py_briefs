# Файл class1.py 

# 01_25 - Объект класса

    <!--
    >>> class Test:
    ...     attr1 = 'атрибут класса'
    ...
    -->


    Пространство имён главного модуля - globals()  
    <!--globals()
        {
            '__name__': '__main__',
            '__doc__': None,
            '__package__': None,
            '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
            '__spec__': None,
            '__annotations__': {},
            '__builtins__': <module 'builtins' (built-in)>,
            'Test': <class '__main__.Test'>
        }
    --> 

    Объект класса Test (Test - идентификатор) 
    Квалифицированное имя класса - __main__ имя модуля - Test - имя класса
    <!--Test
        <class '__main__.Test'>
    -->
    
    Внутреннее пространство имён класса Test - специальный атрибут __dict__
    <!--Test.__dict__
        mappingproxy({
            '__module__': '__main__',
            'attr1': 'атрибут класса',
            '__dict__': <attribute '__dict__' of 'Test' objects>,
            '__weakref__': <attribute '__weakref__' of 'Test' objects>,
            '__doc__': None
        })
        
        Test.__name__
        'Test'
        
        Test.attr1
        'атрибут класса'
    -->
    
# 01_35 - Экземпляр класса

    Создание экземпляра класса - каждый вызов создает новый объект (экземпляр)
    <!--instance = Test()
        instance
        <__main__.Test object at 0x0000025B0108D610>
        
        id(instance)
        2589882635792
        
        id(Test)
        2589881924000
        
        instance_2 = Test()
        id(instance_2)
        2589882636112
    -->
    
    У каждого экземпляра есть своё внутренне пространство имён (изначально пустое)
    Экземпляры класса ссылаются на объект класса от которого они созданы 
    <!--instance.__dict__
        {}
        
        instance.__class__
        <class '__main__.Test'>
        
        id(instance)
        2589882635792
        
        id(instance.__class__)
        2589881924000
        
        id(type(instance))
        2589881924000

        id(Test)
        2589881924000
    
        Test is instance.__class__ is type(instance)
        True
        
        Test is instance.__class__ is instance_2.__class__
        True
    -->
    
    Способы ссылки на объект класса
    ```
        1. Test
        2. instance.__class__
        3. type(instance)

        1. id(Test) - 2589881924000
        2. id(instance.__class__) - 2589881924000
        3. id(type(instance)) - 2589881924000
    ```
    
# 01_47 - Расширение области видимости
    
    Область видимости экземпляра класса расширяется до внетреннего
    пространства имён объекта класса от которого создан экземпляр
    
# 01_48 - Создание атрибутов экземпляра класса

    Подобно словарям (пара ключ = значение)
    Новый атрибут создается только для конкретного экземпляра
    <!--instance.attr_2 = 'атрибут экземпляра'
        
        instance.__dict__
        {'attr_2': 'атрибут экземпляра'}
        
        instance_2.__dict__
        {}
    -->
    
    attr1 из пространства имен Test, attr_2 из пространства имён экземпляра
    <!--instance.attr1
        'атрибут класса'
        instance.attr_2
        'атрибут экземпляра'
    -->
    
    затеняющий атрибут класса
    <!--instance.attr1 = 'атрибут экземпляра, затеняющий атрибут класса'
        instance.attr1
        'атрибут экземпляра, затеняющий атрибут класса'
        
        Test.__dict__
        mappingproxy({
            '__module__': '__main__',
            'attr1': 'атрибут класса',
            ...
        })
        
        instance.__dict__
        {
            'attr_2': 'атрибут экземпляра',
            'attr1': 'атрибут экземпляра, затеняющий атрибут класса'
        }
        
        Test.attr1 = 'новое значение атрибута класса'
        
        instance.attr1
        'атрибут экземпляра, затеняющий атрибут класса'
        
        instance.__class__.attr1
        'новое значение атрибута класса'
        
        instance_2.attr1
        'новое значение атрибута класса'
    -->

# Файл class2.py 
    
# 02_13 - Конструкторы

    Конструктор класса
    <!--class Test:
            def hello():
                print('Привет!')

        Test.__dict__
        mappingproxy({
            '__module__': '__main__',
            'hello': <function Test.hello at 0x00000211B26DAA20>,
            '__dict__': <attribute '__dict__' of 'Test' objects>,
            '__weakref__': <attribute '__weakref__' of 'Test' objects>,
            '__doc__': None
        })
         
        Test.hello()
        Привет!
        
        instance = Test()
        instance.__dict__
        {}
        
        instance.hello
        <bound method Test.hello of <__main__.Test object at 0x00000211B26CD610>>
        
        instance.hello()
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: Test.hello() takes 0 positional arguments but 1 was given
    -->
    
    Метод в общем случае - это облочка для функции, с помощью которой осуществляется подмена вызова.
    При вызове метода от экземпляра, происходит подмена вызова.
        ```
        instance.hello() --> Test.hello(instanse)
        instance.hello() --> instanse.__class__.hello(instanse)
        
        ```
        
# При вызове метода класса от экземпляра, экземпляр класса передается в качестве аргумента этому методу
    <!--class Test:
            def hello():
                print('Hello!')
            def print_arg(arg=None):
                print(arg)
                
        instance = Test()
        
        Test.print_arg
        <function Test.print_arg at 0x000001BDEF44AAC0>        
        
        Test.print_arg()
        None
        
        instance.print_arg
        <bound method Test.print_arg of <__main__.Test object at 0x000001BDEF43DB90>>
        
        instance.print_arg()
        <__main__.Test object at 0x000001BDEF43DB90>
        
        instance
        <__main__.Test object at 0x000001BDEF43DB90>
    -->
    
    В случае если в классе есть методов без параметров, то его нельзя вызвать от экземляра.
    Выход: использовать параметр заглушку: 
    ```
    def hello(): --> def hello(dummy)
    ```
    не желательный способ:
    <!--class Test:
        def hello(dummy):
            print('Hello!')

        instance = Test()
        instance.hello()
        Hello!
    -->

# Файл class3.py
    
# 02_30 - Объединение 2-х (добавление атрибутов экземпляру и вызовы методов)   
    
    __init__ - специальный метод (конструктор), 
    который вызывается в момент создания объекта класса или экземпляра.
    
    __init__(
            первый позиционный параметр, ссылка на объект экземпляра, 
            атрибут экземпляра 1,
            атрибут экземпляра 2,
            ...
        )
        
    <!--class Person:
            def __init__(self, last_name: str, first_name: str):
                self.family = last_name
                self.name = first_name
    
        ivan = Person('Fekistov', 'Inan')
        anna = Person('Dynaevskaia', 'Anna')
    
        ivan
        <__main__.Person object at 0x00000270B56CDA50>
        
        anna
        <__main__.Person object at 0x00000270B56CDB50>
    
        ivan.__dict__
        {'family': 'Fekistov', 'name': 'Inan'}
        
        anna.__dict__
        {'family': 'Dynaevskaia', 'name': 'Anna'}
    
        Person.__dict__
        mappingproxy({
            '__module__': '__main__',
            '__init__': <function Person.__init__ at 0x00000270B56DAA20>,
            '__dict__': <attribute '__dict__' of 'Person' objects>,
            '__weakref__': <attribute '__weakref__' of 'Person' objects>,
            '__doc__': None
        })
    -->