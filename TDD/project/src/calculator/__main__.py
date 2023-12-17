"""
Точка входа.
"""
print('\nТочка входа: __main__ -> start')
print(f'\t{__package__ = }')

from calculator import app
print('\n\tfrom calculator import app')
print(f'\t{app.__package__ = }')
print(f'\t{app = }')
print(f'\t{app.app = }')
print(f'\t{app.app.utils = }')
print(f'\t{app.app.utils.vars.var1 = }')
print(f'\t{app.app.utils.var1 = }')
print(f'\t{app.model.utils = }')
print(f'\t{app.model = }')
print(f'\t{app.model.utils.vars.var1 = }')
print(f'\t{app.model.utils.var1 = }')

from calculator import io
print('\n\tfrom calculator import io')
print(f'\t{io.__package__ = }')
print(f'\t{io.files = }')
print(f'\t{io.files.utils = }')
print(f'\t{io.files.utils.vars.var1 = }')
print(f'\t{io.files.utils.var1 = }')



# 12:14:48 > python -i calculator
# __main__ > start
# >>> import app
# >>> import io
# >>> import utils
# >>> app
# <module 'app' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\app\\__init__.py'>
# >>> io
# <module 'io' (frozen)>
# >>> utils
# <module 'utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\calculator\\utils\\__init__.py'>










# D:\temp\briefs\TDD\project\src
# 19:01:37 > python -i __main__.py
# >>>
# >>> import utils
# >>>
# >>> utils
# <module 'utils' from 'D:\\temp\\briefs\\TDD\\project\\src\\utils\\__init__.py'>
# >>>
# >>> type(utils)
# <class 'module'>v

# НЕВОЗМОЖНАЯ ОПЕРАЦИЯ
# >>> utils.vars
# ...
# AttributeError: module 'utils' has no attribute 'vars'
# >>>

# ВОЗМОЖНАЯ ОПЕРАЦИЯ
# >>> from utils import vars
# >>>
# >>> vars
# <module 'utils.vars' from 'D:\\temp\\briefs\\TDD\\project\\src\\utils\\vars.py'>

# ВОЗМОЖНАЯ ОПЕРАЦИЯ
# >>> import utils.vars

