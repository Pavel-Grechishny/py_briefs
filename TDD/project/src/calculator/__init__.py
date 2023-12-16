"""
Корневой пакет.
"""
print('__init__ > start')
# Импортируем все наши пакеты
from . import app
print('\t__init__ > import app')
from . import io
print('\t__init__ > import io')
from . import utils
print('\t__init__ > import utils')