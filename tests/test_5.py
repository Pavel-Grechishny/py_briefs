from pytest import mark

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


@mark.parametrize('data', 
    [
        ([1,2,3,4,5,6,7,8,9,10],),
        ([1,2,3,4,5,6,7,8,9,10], ['!', '!', '!']),
    ]
)
def test_join_list(data: str):
    print(data)
    print(*data)
    assert join_list(*data)
 
 # D:\temp\briefs
 # 16:41:48 > pytest -v tests\test_5.py
# ==================================================== test session starts =====================================================
# platform win32 -- Python 3.11.3, pytest-7.4.3, pluggy-1.3.0 -- C:\Python311\python.exe
# cachedir: .pytest_cache
# rootdir: D:\temp\briefs
# collected 2 items

# tests/test_5.py::test_join_list[data0] PASSED                                                                           [ 50%]
# tests/test_5.py::test_join_list[data1] FAILED                                                                           [100%]

# ========================================================== FAILURES ==========================================================
# ___________________________________________________ test_join_list[data1] ____________________________________________________

# data = ([1, 2, 3, 4, 5, 6, ...], ['!', '!', '!'])

    # @mark.parametrize('data',
        # [
            # ([1,2,3,4,5,6,7,8,9,10],),
            # ([1,2,3,4,5,6,7,8,9,10], ['!', '!', '!']),
        # ]
    # )
    # def test_join_list(data: str):
        # print(data)
        # print(*data)
# >       assert join_list(*data)

# tests\test_5.py:38:
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# data = [1, 2, 3, 4, 5, 6, ...], sep = ['!', '!', '!']

    # def join_list(data: list[str | int], sep: list[str] = ['\t', '\n']) -> str:
        # """Объединяет элементы списка чередуя разделители."""
        # if not 0 < len(sep) <= 2:
# >           raise ValueError('Допустимо только 2 разделителя.')
# E           ValueError: Допустимо только 2 разделителя.

# tests\test_5.py:6: ValueError
# ---------------------------------------------------- Captured stdout call ----------------------------------------------------
# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['!', '!', '!'])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ['!', '!', '!']
# ================================================== short test summary info ===================================================
# FAILED tests/test_5.py::test_join_list[data1] - ValueError: Допустимо только 2 разделителя.
# ================================================ 1 failed, 1 passed in 0.08s =================================================