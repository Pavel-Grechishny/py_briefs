## Мост ##

> Структурный - взаимосвязь сущностей

Связь между группами


```python
"""Мост"""

from abc import ABC, abstractmethod

class Material(ABC):
    hits: float
    @abstractmethod
    def __str__(self):
        pass

class Straw(Material):
    hits = 0.75
    def __str__(self):
        return 'straw'

class Wood(Material):
    hits = 1.0
    def __str__(self):
        return 'wooden'       

class Cobblestone(Material):
    hits = 1.5
    def __str__(self):
        return 'cobblestone'

class Brick(Material):
    hits = 1.25
    def __str__(self):
        return 'brick'

class Building(ABC):
    base_hitpoints: int
    def __init__(self, material: Material, name: str):
        self.material = material
        self.hitpoints = int(self.base_hitpoints * material.hits)
        self.name = name
    @abstractmethod
    def __str__(self):
        pass

class Watchtower(Building):
    base_hitpoints = 300
    def __str__(self):
        return f'{self.material} watchtower {self.name}: {self.hitpoints}'.title() + ' HP'

class Wall(Building):
    base_hitpoints = 200
    def __str__(self):
        return f'{self.name} Wall ({self.material}): {self.hitpoints} HP'

class Mill(Building):
    base_hitpoints = 100
    def __str__(self):
        return f'{self.material} mill {self.name}: {self.hitpoints} HP'


west_tower = Watchtower(Brick(), 'of the west border')
print(west_tower)

west_tower = Wall(Cobblestone(), 'East')
print(west_tower)

hill_mill = Mill(Wood(), 'on the green hill')
print(hill_mill)

# Brick Watchtower Of The West Border: 375 HP
# East Wall (cobblestone): 300 HP
# wooden mill on the green hill: 100 HP
```