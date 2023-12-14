##Фабрика выбирающая##
> Порождающий - создание объекта

**Фабрика выбирающая:
1. Выбор и донастройка экземпляра

```python
"""Выбирающая фабрика"""

from decimal import Decimal as dec
from random import choice
from dataclasses import dataclass
from datetime import date, datetime as dt
from abc import ABC


def countable_nouns(number: int, nouns: tuple[str, str, str]) -> str:
    """Подставляет существительное с окончанием в зависимости от согласуемого числительного"""
    
    digits_nouns = (
        {1: nouns[0]}
        | dict.fromkeys((2, 3, 4), nouns[1])
        | dict.fromkeys((5, 6, 7, 8, 9, 0, 11, 12, 13, 14), nouns[2])
    )
    # print(digits_nouns)
    last_digit, two_last_digit = number % 10, number % 100
    # print(last_digit, two_last_digit)
    # print(digits_nouns.get(two_last_digit))
    return digits_nouns.get(two_last_digit) or digits_nouns[last_digit]
    

@dataclass
class Person(ABC):
    name: str
    birthdate: date
    
    @property
    def age(self) -> int:
        return (date.today() - self.birthdate).days // 365
        
    def __str__(self):
        age = self.age
        noun = countable_nouns(age, ('год', 'года', 'лет'))
        return f'{self.name}: {age} {noun}'


@dataclass
class Employee(Person):
    position: str
    income: dec
    
    def __str__(self):
        return (
            super().__str__() + 
            f', {self.position} ({self.income:.2f})'
        )
        
@dataclass
class Candidate(Person):
    cv: bytes = None
    expert1: bool = False
    expert2: bool = False
    final: bool = False
    
    def __bool__(self):
        return self.expert1 and self.expert2 and self.final
       
    def __str__(self):
        return (
            super().__str__() + 
            f', {self.expert1}-{self.expert2}-{self.final}'
        )
        
class Factory:
    """Определяет правила приёма кандидата, этапы проведения собеседований и найм кандидата"""
    def __init__(self, age_min: int = 18, age_max: int = 58):
        self.age_min = age_min
        self.age_max = age_max
        self.choices: list[bool] = [False, True]
        
    @staticmethod
    def create_candidate(name: str, birthdate: str) -> Candidate:
        person = Candidate(
            name,
            dt.strptime(birthdate, '%d.%m.%Y').date()
        )
        # with open('cv.pdf', 'rb') as filein:
            # person.cv = filein.read()
        return person
        
    def tech_meeting1(self, candidate: Candidate) -> None:
        candidate.expert1 = choice(self.choices)
        
    def tech_meeting2(self, candidate: Candidate) -> None:
        candidate.expert2 = choice(self.choices)
        
    def final_meeting(self, candidate: Candidate) -> None:
        candidate.final = choice((False, candidate.expert1 and candidate.expert2))
        
    def hire_candidate(
        self,
        person: Candidate,
        position: str,
        income: str
    ) -> Employee | Candidate:
        if self.age_min <= person.age <= self.age_max:
            if all((person.expert1, person.expert2, person.final)):
                emp = Employee(
                    person.name,
                    person.birthdate,
                    position,
                    dec(income)
                )
                ...
                return emp
        return person


# >>> hr = Factory()
# >>> hr.__dict__
# {'age_min': 18, 'age_max': 58, 'choices': [False, True]}
# >>>
# >>> egor = hr.create_candidate('Егор', '05.05.1990')
# >>>
# >>> hr.tech_meeting1(egor)
# >>> hr.tech_meeting2(egor)
# >>> hr.final_meeting(egor)
# >>>
# >>> egor = hr.hire_candidate(egor, 'Python dev junior', '82540.00')
# >>> egor.__dict__
# {'name': 'Егор', 'birthdate': datetime.date(1990, 5, 5), 'cv': None, 'expert1': False, 'expert2': False, 'final': False}
# >>>
# >>> hr.tech_meeting1(egor)
# >>> egor.__dict__
# {'name': 'Егор', 'birthdate': datetime.date(1990, 5, 5), 'cv': None, 'expert1': True, 'expert2': False, 'final': False}
# >>> hr.tech_meeting2(egor)
# >>> egor.__dict__
# {'name': 'Егор', 'birthdate': datetime.date(1990, 5, 5), 'cv': None, 'expert1': True, 'expert2': True, 'final': False}
# >>> hr.final_meeting(egor)
# >>> egor.__dict__
# {'name': 'Егор', 'birthdate': datetime.date(1990, 5, 5), 'cv': None, 'expert1': True, 'expert2': True, 'final': False}
# >>> hr.final_meeting(egor)
# >>> egor.__dict__
# {'name': 'Егор', 'birthdate': datetime.date(1990, 5, 5), 'cv': None, 'expert1': True, 'expert2': True, 'final': True}
```