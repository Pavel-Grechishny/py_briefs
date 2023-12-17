"""
Корневой пакет.
"""
print('\nИнициализация корневого пакета: __init__ > start')

# Импортируем все наши пакеты
from . import app
from . import io
from . import utils


# D:\temp\briefs\TDD\project\src
 # 13:54:45 > python -m calculator

# Инициализация корневого пакета: __init__ > start
        # app = <module 'calculator.app.app' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\app\\app.py'>
                # app.utils = <module 'calculator.utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>
        # model = <module 'calculator.app.model' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\app\\model.py'>
                # model.utils = <module 'calculator.utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>
        # files = <module 'calculator.io.files' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\io\\files.py'>
                # files.utils = <module 'calculator.utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>

# Точка входа: __main__ -> start
        # __package__ = 'calculator'

        # from calculator import app
        # app.__package__ = 'calculator.app'
        # app = <module 'calculator.app' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\app\\__init__.py'>
        # app.app = <module 'calculator.app.app' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\app\\app.py'>
        # app.app.utils = <module 'calculator.utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>
        # app.app.utils.vars.var1 = 123
        # app.app.utils.var1 = 123
        # app.model.utils = <module 'calculator.utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>
        # app.model = <module 'calculator.app.model' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\app\\model.py'>
        # app.model.utils.vars.var1 = 123
        # app.model.utils.var1 = 123

        # from calculator import io
        # io.__package__ = 'calculator.io'
        # io.files = <module 'calculator.io.files' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\io\\files.py'>
        # io.files.utils = <module 'calculator.utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>
        # io.files.utils.vars.var1 = 123
        # io.files.utils.var1 = 123