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

## 元组
### 创建元组
emptyTuple = ()
print(emptyTuple)
# 会输出 ()
oneTuple = ('a',)
print(oneTuple)
# 会输出 ('a',)
normalTuple = ('a', 'b', 'c')
print(normalTuple)
# 会输出 ('a', 'b', 'c')

normalTuple = ('A', 'B', 'C')
print(normalTuple)
# 会输出 ('A', 'B', 'C')
a, b, c = normalTuple
print(a, b, c)
# 会输出 A B C

## 字典
### 创建字典
emptyDict = {}
print(emptyDict)
# 会输出 {}
normalDict = {'A': 'aaa', 'B': 'bbb'}
print(normalDict)
# 会输出 {'A': 'aaa', 'B': 'bbb'}

### 操作元组
modifyDict = {'A': 'aaa', 'B': 'bbb'}
modifyDict['A'] = 'aaaA'
modifyDict['C'] = 'ccc'
print(modifyDict)
# 会输出 {'A': 'aaaA', 'B': 'bbb', 'C': 'ccc'}

updateDict = {'A': 'aaa', 'B': 'bbb'}
updateDict.update({'C': 'ccc', 'B': 'bbbB'})
print(updateDict)
# 会输出 {'A': 'aaa', 'B': 'bbbB', 'C': 'ccc'}

clearDict = {'A': 'aaa', 'B': 'bbb'}
clearDict.clear()
print(clearDict)
# 会输出 {}

keysDict = {1: '111', '2': 222}
print(keysDict.keys())
# 会输出 dict_keys([1, '2'])
print(keysDict.values())
# 会输出 dict_values(['111', 222])
print(keysDict.items())
# 会输出 dict_items([(1, '111'), ('2', 222)])

## 集合
### 创建集合
normalSet = {0, 1, 2, 3, 4, 5, 6}
print(normalSet)
# 会输出 {0, 1, 2, 3, 4, 5, 6}

emptySet = set()
print(emptySet)
# 会输出 set()

### 操作集合
aSet = {1, 2}
bSet = {2, 3}
abSet = {1, 2, 3}

print(aSet & bSet)
print(aSet.intersection(bSet))
# 会输出 {2}
print(aSet | bSet)
print(aSet.union(bSet))
# 会输出 {1, 2, 3}
print(aSet - bSet)
print(aSet.difference(bSet))
# 会输出 {1}
print(aSet ^ bSet)
print(aSet.symmetric_difference(bSet))
# 会输出 {1, 3}
print(aSet <= abSet)
print(aSet.issubset(abSet))
# 会输出 True
print(abSet <= abSet)
# 会输出 True
print(abSet < abSet)
# 会输出 False
print(abSet >= bSet)
print(abSet.issuperset(bSet))
# 会输出 True
print(abSet >= abSet)
# 会输出 True
print(abSet > abSet)
# 会输出 False
