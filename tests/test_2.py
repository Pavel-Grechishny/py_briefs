def test_one():
    print('test_one')
    assert 1

def test_two():
    print('test_two')
    assert False

def test_three():
    print('test_three')
    assert True
    
# D:\temp\briefs\tests
 # 14:10:00 > pytest -v test_2.py
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs\tests
# collected 3 items

# test_2.py::test_one PASSED                                                                   [ 33%]
# test_2.py::test_two FAILED                                                                   [ 66%]
# test_2.py::test_three PASSED                                                                 [100%]

# ============================================ FAILURES =============================================
# ____________________________________________ test_two _____________________________________________

    # def test_two():
        # print('test_two')
# >       assert False
# E       assert False

# test_2.py:7: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# test_two
# ===================================== short test summary info =====================================
# FAILED test_2.py::test_two - assert False
# =================================== 1 failed, 2 passed in 0.07s ===================================


def test_four():
    raise ValueError('test_four')

# D:\temp\briefs\tests
 # 14:13:26 > pytest -v test_2.py
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs\tests
# collected 4 items

# test_2.py::test_one PASSED                                                                   [ 25%]
# test_2.py::test_two FAILED                                                                   [ 50%]
# test_2.py::test_three PASSED                                                                 [ 75%]
# test_2.py::test_four FAILED                                                                  [100%]

# ============================================ FAILURES =============================================
# ____________________________________________ test_two _____________________________________________

    # def test_two():
        # print('test_two')
# >       assert False
# E       assert False

# test_2.py:7: AssertionError
# -------------------------------------- Captured stdout call ---------------------------------------
# test_two
# ____________________________________________ test_four ____________________________________________

    # def test_four():
# >       raise ValueError('test_four')
# E       ValueError: test_four

# test_2.py:42: ValueError
# ===================================== short test summary info =====================================
# FAILED test_2.py::test_two - assert False
# FAILED test_2.py::test_four - ValueError: test_four
# =================================== 2 failed, 2 passed in 0.08s ===================================