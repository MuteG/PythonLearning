## 连接
multiLineStr = 'hell' + \
    'o, w' + \
    'orld'
print(multiLineStr)
# 会输出 hello, world

## 条件分支
### 条件控制
furry = True
small = True
if furry:
    if small:
        print(" It' s a cat.")
    else:
        print(" It' s a bear!")
else:
    if small:
        print(" It' s a skink!")
    else:
        print(" It' s a human. Or a hairless bear.")
# 会输出 It' s a cat.

## while 循环
whileList = []
whileNum = 1
while True:
    if len(whileList) == 5:
        break
    if whileNum % 2 == 0:
        whileList.append(whileNum)
    whileNum += 1
print(whileList)
# 会输出 [2, 4, 6, 8, 10]

whileList = []
whileNum = 1
while whileNum < 10:
    if len(whileList) == 5:
        break
    if whileNum % 2 == 0:
        whileList.append(whileNum)
    whileNum += 1
else:
    whileList.append(9)
print(whileList)
# 会输出 [2, 4, 6, 8, 9]

## for 循环
forList = []
for forNum in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if len(forList) == 5:
        break
    if forNum % 2 == 0:
        forList.append(forNum)
else:
    forList.append(11)
print(forList)
# 会输出 [2, 4, 6, 8, 10, 11]
