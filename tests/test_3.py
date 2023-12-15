from pytest import mark

# @mark.xfail - тест который запланирован к провалу

@mark.xfail
def test_fail_true():
    """Запланирован к провалу, но выполняется."""
    assert True
    
@mark.xfail
def test_fail_false():
    """Запланирован к провалу и провален."""
    assert False

# В отчет FAILURES не попадают
# tests/test_3.py::test_fail_true XPASS
# tests/test_3.py::test_fail_false XFAIL  

# D:\temp\briefs
 # 15:00:38 > pytest -v tests\test_3.py
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs
# collected 2 items

# tests/test_3.py::test_fail_true XPASS                                                        [ 50%]
# tests/test_3.py::test_fail_false XFAIL                                                       [100%]

# ================================== 1 xfailed, 1 xpassed in 0.06s ==================================