# 变量声明
a = 11
print(a)
b = a
print(b)

# 类型
print(type(True))
print(type(1))
print(type(1.0))
print(type('1'))

# 基数
print('0x0010 =', 0x0010)

# 数值计算
print('5 / 2 =', 5 / 2)
print('5 // 2 =', 5 // 2)
print('5 % 2 =', 5 % 2)
print('5 ** 2 =', 5 ** 2)

# 类型转换
print("bool(2) =>", bool(2))
print('bool(0.0) =>', bool(0.0))
print("bool('False') =>", bool('False'))
print("bool('') =>", bool(''))
print('int(True) =>', int(True))
print('int(1.9) =>', int(1.9))
print("int('010') =>", int('010'))
print('float(True) =>', float(True))
print('float(0) =>', float(0))
print("float('1.0') =>", float(1.0))
print("str(True) =>", str(True))
print("str(1) =>", str(1))
print("str(1.0) =>", str(1.0))

# 字符串
print('创建', 'A' * 4 + 'B')
print('分片', 'ABCDEFGH'[1:-1:2])
print('分割', 'A,B,C'.split(','))
print('分割（不指定分隔符）', 'A B\tC\nD'.split())
print('合并', ', '.join(['A', 'B', 'C']))
print('rfind', 'ABCABC'.rfind('A'))
print('replace', 'ABCABC'.replace('A', 'XX', 1))
