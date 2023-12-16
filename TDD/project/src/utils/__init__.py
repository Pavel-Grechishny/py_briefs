# Вариант 1 без инструкции __all__ в vars.py
# import vars

# Вариант 2 с инструкцией __all__ в vars.py
from .vars import *

# D:\temp\briefs\TDD\project\src
# 19:16:37 > python -i __main__.py
# >>>
# >>> import utils
# >>>
# >>> utils.vars
# <module 'utils.vars' from 'D:\\temp\\briefs\\TDD\\project\\src\\utils\\vars.py'>

# ДОСТУПНЫЙ ОБЪЕКТ
# >>> utils.var1
# 123

# НЕ ДОСТУПНЫЙ ОБЪЕКТ
# >>> utils.var2
# ...
# AttributeError: module 'utils' has no attribute 'var2'. Did you mean: 'var1'?