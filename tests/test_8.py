from pytest import fixture
from pathlib import Path
from sys import path

path.append(r'D:\temp\scripts\oop')
journal = Path(path[0]) / 'test_8.log'

import methods3

@fixture
def new_cat() -> methods3.Cat:
    return methods3.Cat()

def log(data) -> None:
    with open(journal, 'a', encoding='UTF-8') as fileout:
        print(data, file=fileout)

def test_meow(new_cat):
    log(f'test_meow: {id(new_cat) = }')
    assert len(new_cat.meow()) == 3

def test_hungry(new_cat):
    log(f'test_hungry: {id(new_cat) = }')
    assert 7 <= len(new_cat.hungry()) <= 15

def test_reproduce_count(new_cat):
    log(f'test_reproduce_count: {id(new_cat) = }')
    assert 2 <= len(new_cat.reproduce()) <= 4

def test_reproduce(new_cat):
    log(f'test_reproduce: {id(new_cat) = }')
    assert all(map(lambda kitten: isinstance(kitten, methods3.Cat),
        new_cat.reproduce()
    ))
        
# D:\temp\briefs
 # 16:19:31 > pytest -v tests\test_7.py
# =================================== test session starts ====================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs
# collected 4 items

# tests/test_7.py::TestCat::test_meow PASSED                                            [ 25%]
# tests/test_7.py::TestCat::test_hungry PASSED                                          [ 50%]
# tests/test_7.py::TestCat::test_reproduce_count PASSED                                 [ 75%]
# tests/test_7.py::TestCat::test_reproduce PASSED                                       [100%]

# ==================================== 4 passed in 0.02s =====================================