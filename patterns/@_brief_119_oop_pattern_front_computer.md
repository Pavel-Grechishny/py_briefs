## Фасад ##

> Структурный - взаимосвязь сущностей

```python
"""Фасад"""

class CPU:
    """Центральный процессор"""
    @staticmethod
    def cooling():
        print('Запуск куллера ЦП')
    
    @staticmethod
    def read_register(register: str):
        print(f'Чтение регистра {register}')
    
    @staticmethod
    def execute():
        print(f'Запуск процесора')


class RAM:
    """Оперативная память"""
    @staticmethod
    def load(data: str):
        print(f'Чтение данных из ОП {data}')
        return ''.join(bin(ord(ch))[2:] for ch in data).upper()


class Drive:
    """Жесткий диск"""
    @staticmethod
    def read(data: str):
        print(f'Чтение данных из Диска {data}')
        return ''.join(hex(ord(ch))[2:] for ch in data).upper()


class Computer:
    """Фасад для компонентов компьютера - Интерфейс"""
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.drive = Drive()
    
    def start(self):
        self.cpu.cooling()
        self.cpu.execute()
        hex_data = self.drive.read('MBR: section 1')
        bin_data = self.ram.load(hex_data)
        self.cpu.read_register(bin_data)


# >>> pc = Computer()
# >>> pc.start()
# Запуск куллера ЦП
# Запуск процесора
# Чтение данных из Диска MBR: section 1
# Чтение данных из ОП 4D42523A2073656374696F6E2031
# Чтение регистра 1101001000100110...011110001

