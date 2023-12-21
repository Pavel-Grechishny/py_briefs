# Визуальное представление пакета
# │
# ├───packages
# │   └──extra
# │      │   iota.py
# │      │   __init__.py
# │      │
# │      ├───good
# │      │   │   alpha.py
# │      │   │   beta.py
# │      │   │
# │      │   └───best
# │      │           sigma.py
# │      │           tau.py
# │      │
# │      └───ugly
# │              omega.py
# │              psi.py
# ├───prog
# │   └──main.py

# # Для файла main.py 
# from sys import path
# # изменение переменной path
# path.append('..\\packages') 
# # Можем заархивировать вместе с extra
# import extra

# extra.iota.func()
# extra.good.alpha.func()
# extra.good.beta.func()
# extra.good.alpha.best.sigma.func()
# extra.good.alpha.best.tau.func()
# extra.ugly.omega.func()
# extra.ugly.psi.func()
