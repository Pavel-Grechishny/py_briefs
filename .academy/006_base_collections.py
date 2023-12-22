from collections import OrderedDict # в отличии от dict запоминает порядок встаки ключей
from collections import defaultdict # предоставляет значения по умолчанию для ключей
from collections import ChainMap    # блок с множеством словарей с возможностью поиска по ключу по всем словарям


string = 'qwerty'
string_type = str(string)
tuple_type = tuple(string)
list_type = list(string)
dict_type = dict(enumerate(string, 1))
set_type = set(string)
frozenset_type = frozenset(string)
bytearray_type = bytearray(range(5))

