""" Модуль struct. Обзор. """

# Общая форма метода pack() - упаковка
# obj = struct.pack(format, v1, v2, ...)

# Общая форма метода unpack() - распаковка
# obj = struct.unpack(format, buffer)

import struct

# Упаковать / распокавать список чисел


def packed(list_nums: list[int]) -> str:
    return struct.pack(f'>{len(list_nums)}i', *list_nums)

def unpacked(packed_object: str) -> tuple[int, ...]:
    return struct.unpack(f'>{20}i', packed_object)


list_numbers = [number for number in range(1, 21)]
pack_numbers = packed(list_numbers)
list_numbers = list(unpacked(pack_numbers))

# pack_numbers
# b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\
#     x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\
#     x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x0e\x00\x00\x00\x0f\x00\x00\
#     x00\x10\x00\x00\x00\x11\x00\x00\x00\x12\x00\x00\x00\x13\x00\x00\x00\x14'

# list_numbers
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Размер упакованного объекта
size_pack = struct.calcsize(f'>{20}i')
# size_pack
# 80