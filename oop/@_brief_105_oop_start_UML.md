## Основы UML ##

UML – Unified Modelling Language.
UML - инструмент для моделирования, используя который можно заниматься проектированием до начала написания кода.
UML - используется в контексте проектирования архитектуры.

1. [PlanUML](https://plantuml.com/ru/)
2. [Book UML](http://book.uml3.ru/content)

### Диаграммы ###

1. Статические
2. Динамические

> Текстовое описание диаграмм с последующим рендерингом в изображение

### Файл - agregation2.puml ###
>...
### Файл - @_brief_106.puml ###
```
@startuml

!theme sketchy-outline
scale 3

class Product {
    +{static}date_format: str
    +name: str
    +produced: date
    +expired: date
    __init__()
    __repr__()
    +is_expired(): bool
}

class Fridge {
    #camera
    __init__()
    __iter__()
    __len__()
    __getitem__()
    __delitem__()
    __repr__()
    +put()
    +clear_expired()
}

Fridge o-left- Product

@enduml
```