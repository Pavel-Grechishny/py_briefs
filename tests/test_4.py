def join_list(data: list[str | int], sep: list[str] = ['\t', '\n']) -> str:
    """Объединяет элементы списка чередуя разделители.""" 
    if not 0 < len(sep) <= 2:
        raise ValueError('Допустимо только 2 разделителя.')
    
    text = ''
    length = len(data)
    for i in range(length):
        if i == length - 1:
            break
        text += str(data[i]) + sep[0]
        sep.reverse()
    text += str(data[length - 1]) 
    return text
 
# >>> print(join_list([1,2,3,4,5,6,7,8,9,10]))
# 1       2
# 3       4
# 5       6
# 7       8
# 9       10
# >>> print(join_list([1,2,3,4,5,6,7,8,9,10], ['!', '!', '!']))
# ...
# ValueError: Допустимо только 2 разделителя


def test_join_list_1():
    assert join_list([1,2,3,4,5,6,7,8,9,10])
    
def test_join_list_2():
    assert join_list([1,2,3,4,5,6,7,8,9,10], ['!', '!', '!'])
    
# ======================================= test session starts =======================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs
# collected 2 items

# tests/test_4.py::test_join_list_1 PASSED                                                     [ 50%]
# tests/test_4.py::test_join_list_2 FAILED                                                     [100%]

# ============================================ FAILURES =============================================
# ________________________________________ test_join_list_2 _________________________________________

    # def test_join_list_2():
# >       assert join_list([1,2,3,4,5,6,7,8,9,10], ['!', '!', '!'])

# tests\test_4.py:31:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# data = [1, 2, 3, 4, 5, 6, ...], sep = ['!', '!', '!']

    # def join_list(data: list[str | int], sep: list[str] = ['\t', '\n']) -> str:
        # """Объединяет элементы списка чередуя разделители."""
        # if not 0 < len(sep) <= 2:
# >           raise ValueError('Допустимо только 2 разделителя.')
# E           ValueError: Допустимо только 2 разделителя.

# tests\test_4.py:4: ValueError
# ===================================== short test summary info =====================================
# FAILED tests/test_4.py::test_join_list_2 - ValueError: Допустимо только 2 разделителя.
# =================================== 1 failed, 1 passed in 0.06s ===================================