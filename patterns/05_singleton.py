"""Одиночка"""

from typing import Self

class Singleton:
    
    __instanse: Self = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls, *args, **kwargs)
            return cls.__instanse
        else:
            return cls.__instanse


# >>> singleton_1 = Singleton()
# >>> singleton_1
# <__main__.Singleton object at 0x0000013B2E514410>
# >>>
# >>> singleton_2 = Singleton()
# >>> singleton_2
# <__main__.Singleton object at 0x0000013B2E514410>