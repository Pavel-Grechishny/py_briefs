##Строитель##
> Порождающий - создание объекта

Предоставляет методы для настройки какого либо объекта.
Отличие от фабрик - методы могут вызываться пошагово

```python
"""Строитель"""

from pathlib import Path
from sys import path
from typing import Self


class HTMLTag:
    """Описывает HTML тег, который может содержать вложенные теги"""
    
    default_indent_spaces: int = 4
    
    def __init__(self, name: str, value: str = ''):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []
    
    # setter
    def nested(self, html_tag: Self) -> None:
        """Добавляет вложенный тег к текущему"""
        self.__nested.append(html_tag)
        
    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами"""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f'{margin}<{self.name}>{self.value}'
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f'{eol}</{self.name}>'
        return result
        
    def __str__(self):
        return self.__str(0)
        
    # В данной реализации не целесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = '') -> 'HTMLBuilder':
        return HTMLBuilder(name, value)


class HTMLBuilder:
    """Предоставляет методы для пошаговой инициализации экземпляра HTMLTag"""
    
    def __init__(self, root: HTMLTag | str, value: str = '', *, parent: Self = None):
        if isinstance(root, HTMLTag):
            pass
        elif isinstance(root, str):
            root = HTMLTag(root, value)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')
        self.root: HTMLTag = root
        self.__parent: Self = parent
        
    def nested(self, name: str, value: str = '') -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега"""
        tag = HTMLTag(name, value)
        self.root.nested(tag)
        return HTMLBuilder(tag, parent=self)
        
    def sibling(self, name: str, value: str = '') -> Self:
        """Добавляет вложенный тег к текущему и возвращает текущий строитель"""
        tag = HTMLTag(name, value)
        self.root.nested(tag)
        return self
        
    def build(self) -> HTMLTag:
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()

 
body = HTMLTag.create('body')\
    .sibling('div')\
    .sibling('div')\
    .sibling('div')\
    .sibling('div')\
    .sibling('div')\
    .build()
print(body)

body = HTMLTag.create('body')\
    .nested('div')\
    .nested('div')\
    .nested('div')\
    .nested('div')\
    .nested('div')\
    .build()
print(body)

(Path(path[0]) / 'builder1.html').write_text(str(body), encoding='utf-8')

# <body>
    # <div></div>
    # <div></div>
    # <div></div>
    # <div></div>
    # <div></div>
# </body>
# <body>
    # <div>
        # <div>
            # <div>
                # <div>
                    # <div></div>
                # </div>
            # </div>
        # </div>
    # </div>
# </body>

```

