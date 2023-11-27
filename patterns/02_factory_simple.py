class Person:

    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name
        
    def __repr__(self):
        return f'{self.name} ({self.id})'
        
        
        
class PersonFactory:
    """Создает и нумерует экземпляры класса Person используя атрибут экземпляра"""
    
    def __init__(self):
        self.id = 0
        
    def create(self, name: str) -> Person:
        self.id += 1
        return Person(self.id, name)
        
        
        
class PersonFactoryCommon:
    """Создает и нумерует экземпляры класса Person используя поле класса"""
    
    id_ = 0
    
    @classmethod
    def create(cls, name: str) -> Person:
        cls.id_ += 1
        return Person(cls.id_, name)
        
        
# >>> pf = PersonFactory()
# >>> p1 = pf.create('Aleksey')
# >>> p2 = pf.create('Victor')
# >>> p3 = pf.create('Oleg')
# >>> print(p1, p2, p3, sep='\n')
# Aleksey (1)
# Victor (2)
# Oleg (3)
# >>>
# >>> pf2 = PersonFactory()
# >>> p4 = pf2.create('Aleksey')
# >>> p5 = pf2.create('Victor')
# >>> p6 = pf2.create('Oleg')
# >>> print(p4, p5, p6, sep='\n')
# Aleksey (1)
# Victor (2)
# Oleg (3)
# >>>
# >>>
# >>> pf3 = PersonFactoryCommon()
# >>> p7 = pf3.create('Aleksey')
# >>> p8 = pf3.create('Victor')
# >>> p9 = pf3.create('Oleg')
# >>> print(p7, p8, p9, sep='\n')
# Aleksey (1)
# Victor (2)
# Oleg (3)
# >>> pf4 = PersonFactoryCommon()
# >>> p10 = pf4.create('Aleksey')
# >>> p11 = pf4.create('Victor')
# >>> p12 = pf4.create('Oleg')
# >>> print(p10, p11, p12, sep='\n')
# Aleksey (4)
# Victor (5)
# Oleg (6)