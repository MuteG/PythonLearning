# 列表
# 创建列表
strList = ['a', 'b']
print(strList)
strList = list('cdef')
print(strList)
intList = [1, 2]
print(intList)
mixList = [strList, True, intList]
print(mixList)

# 基本操作
print(mixList[2])
mixList[1] = False
print(mixList)
mixList.append(3)
print(mixList)
mixList.remove(intList)
print(mixList)

appendList = ['A', 'B']
appendList.append('C')
print(appendList)

extendList = ['A', 'B']
extendList += ['C', 'D']
print(extendList)

insertList = ['A', 'B']
insertList.insert(1, 'C')
print(insertList)

delList = ['A', 'B', 'C']
del delList[1]
print(delList)

removeList = ['A', 'B', 'C']
removeList.remove('B')
print(removeList)

popList = ['A', 'B', 'C', 'D']
print(popList.pop())
# 会输出 D
print(popList)
# 会输出 ['A', 'B', 'C']
print(popList.pop(1))
# 会输出 B
print(popList)
# 会输出 ['A', 'C']

indexList = ['A', 'B', 'C']
print(indexList.index('B'))
# 会输出 1

inList = ['A', 'B', 'C']
print('B' in inList)
# 会输出 True
print('D' in inList)
# 会输出 False

countList = ['A', 'B', 'C', 'B']
print(countList.count('D'))
# 会输出 0
print(countList.count('C'))
# 会输出 1
print(countList.count('B'))
# 会输出 2

sortList = ['B', 'A', 'C']
sortList.sort()
print(sortList)

sortList = ['B', 'A', 'C']
sortedList = sorted(sortList)
print(sortList)
# 会输出 ['B', 'A', 'C']
print(sortedList)
# 会输出 ['A', 'B', 'C']

lenList = ['B', 'A', 'C']
print(len(lenList))
# 会输出 3

sortList = ['B', 'A', 'C']
copyList = sortList.copy()
sortList.sort()
print(sortList)
# 会输出 ['A', 'B', 'C']
print(copyList)
# 会输出 ['B', 'A', 'C']