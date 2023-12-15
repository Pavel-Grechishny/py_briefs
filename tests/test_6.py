from pytest import mark
from sys import path

# импорт калькулятора
path.append(r'D:\temp\scripts\base')
from functions4 import calculator

data = (
    (1, 1, '+', 2),
    (1, 0, '*', 0),
    (1, 99, '+', 100),
    (18, 3, '/', 6.0),
    (10, 2, '//', 5),
    (11, 3, '%', 2),
    (1, 0, '/', float('inf')),
)


# хотим проверить корректность работы калькулятора
@mark.parametrize('n1,n2,op,res', data)
def test_calculator(n1: int, n2: int, op: str, res: float):
    assert calculator(n1, n2, op) == res
    
 # 17:21:20 > pytest -v tests\test_6.py
# ================================================= test session starts ==================================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs
# collected 7 items

# tests/test_6.py::test_calculator[1-1-+-2] PASSED                                                                  [ 14%]
# tests/test_6.py::test_calculator[1-0-*-0] PASSED                                                                  [ 28%]
# tests/test_6.py::test_calculator[1-99-+-100] PASSED                                                               [ 42%]
# tests/test_6.py::test_calculator[18-3-/-6.0] PASSED                                                               [ 57%]
# tests/test_6.py::test_calculator[10-2-//-5] FAILED                                                                [ 71%]
# tests/test_6.py::test_calculator[11-3-%-2] FAILED                                                                 [ 85%]
# tests/test_6.py::test_calculator[1-0-/-inf] PASSED                                                                [100%]

# ======================================================= FAILURES =======================================================
# ______________________________________________ test_calculator[10-2-//-5] ______________________________________________

# n1 = 10, n2 = 2, op = '//', res = 5

    # @mark.parametrize('n1,n2,op,res', data)
    # def test_calculator(n1: int, n2: int, op: str, res: float):
# >       assert calculator(n1, n2, op) == res
# E       AssertionError: assert None == 5
# E        +  where None = calculator(10, 2, '//')

# tests\test_6.py:22: AssertionError
# ______________________________________________ test_calculator[11-3-%-2] _______________________________________________

# n1 = 11, n2 = 3, op = '%', res = 2

    # @mark.parametrize('n1,n2,op,res', data)
    # def test_calculator(n1: int, n2: int, op: str, res: float):
# >       assert calculator(n1, n2, op) == res
# E       AssertionError: assert None == 2
# E        +  where None = calculator(11, 3, '%')

# tests\test_6.py:22: AssertionError
# =============================================== short test summary info ================================================
# FAILED tests/test_6.py::test_calculator[10-2-//-5] - AssertionError: assert None == 5
# FAILED tests/test_6.py::test_calculator[11-3-%-2] - AssertionError: assert None == 2
# ============================================= 2 failed, 5 passed in 0.09s ==============================================