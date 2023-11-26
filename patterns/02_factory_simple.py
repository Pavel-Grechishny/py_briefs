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