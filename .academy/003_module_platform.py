import platform

print(f'{platform.platform() = }')
print(f'{platform.platform(1) = }')
print(f'{platform.platform(0, 1) = }')
print(f'{platform.machine() = }')
print(f'{platform.processor() = }')
print(f'{platform.system() = }')
print(f'{platform.version() = }')
print(f'{platform.python_implementation() = }')
print(f'{platform.python_version_tuple() = }')

# 11:09:22 > python -i 003_module_platform.py
# platform.platform() = 'Windows-10-10.0.19045-SP0'
# platform.platform(1) = 'Windows-10-10.0.19045-SP0'
# platform.platform(0, 1) = 'Windows-10'
# platform.machine() = 'AMD64'
# platform.processor() = 'Intel64 Family 6 Model 158 Stepping 11, GenuineIntel'
# platform.system() = 'Windows'
# platform.version() = '10.0.19045'
# platform.python_implementation() = 'CPython'
# platform.python_version_tuple() = ('3', '11', '3')
