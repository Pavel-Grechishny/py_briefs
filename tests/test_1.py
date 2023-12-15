def test_one():
    assert 1

def test_two():
    assert False

# Названия функций test_*()
# Названия модулей test_*.py or *_test.py
# pytest test_1.py
# pytest -v test_1.py


# D:\temp\briefs\tests
 # 12:27:52 > pytest test_1.py
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0
# rootdir: D:\temp\briefs\tests
# collected 2 items

# test_1.py .F                                                                                 [100%]

# ============================================ FAILURES =============================================
# ____________________________________________ test_two _____________________________________________

    # def test_two():
# >       assert False
# E       assert False

# test_1.py:5: AssertionError
# ===================================== short test summary info =====================================
# FAILED test_1.py::test_two - assert False
# =================================== 1 failed, 1 passed in 0.06s ===================================


# D:\temp\briefs\tests
 # 14:05:15 > pytest -v test_1.py
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs\tests
# collected 2 items

# test_1.py::test_one PASSED                                                                   [ 50%]
# test_1.py::test_two FAILED                                                                   [100%]

# ============================================ FAILURES =============================================
# ____________________________________________ test_two _____________________________________________

    # def test_two():
# >       assert False
# E       assert False

# test_1.py:5: AssertionError
# ===================================== short test summary info =====================================
# FAILED test_1.py::test_two - assert False
# =================================== 1 failed, 1 passed in 0.08s ===================================