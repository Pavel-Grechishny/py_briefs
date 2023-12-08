"""
Инициализирующий модуль.
"""

from pathlib import Path
from sys import path

ROOT_DIR = Path(path[0])
DB_PATH = ROOT_DIR / 'data'
FILE_HUMANS = DB_PATH / 'humans.txt' 

import model.folder1.mod1


if __name__ == '__main__':
    print(f'{ROOT_DIR=}')
    print(f'{FILE_HUMANS=}')
    print(f'{DB_PATH=}')