from sys import path

path.append(r'D:\temp\scripts\oop')
import methods3

class TestCat:
    instance = methods3.Cat()
    
    def test_meow(self):
        assert len(self.instance.meow()) == 3

    def test_hungry(self):
        assert 7 <= len(self.instance.hungry()) <= 15

    def test_reproduce_count(self):
        assert 2 <= len(self.instance.reproduce()) <= 4

    def test_reproduce(self):
        assert all(map(lambda kitten: isinstance(kitten, methods3.Cat),
            self.instance.reproduce()
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