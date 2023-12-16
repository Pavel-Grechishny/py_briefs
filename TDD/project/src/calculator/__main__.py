"""
Точка входа.
"""
print('__main__ > start')

print(app.model)
print(app.model.utils)










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

