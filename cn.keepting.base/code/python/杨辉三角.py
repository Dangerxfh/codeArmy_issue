
#打印杨辉三角
#普通思路: level是当前行，indexLevel是下一行，递推式：indexLevel[j]=level[j]+level[j-1]
def san(num):

    level=[1]
    indexLevel = [];
    for i in range(0,num):
        for j in range(1,len(level)):
            indexLevel[j]=level[j]+level[j-1]
        indexLevel.append(1)
        print(indexLevel)
        level=indexLevel.copy()
#调用
san(8)

#打印结果如下：
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]

#=================================================================================

#增强版 ：利用zip+生成器巧妙实现
def san2(num):
    level = [1]
    for i in range(num):
        yield level
        level = [i + j for i, j in zip([0, *level], [*level, 0])]

#调用
for n in san2(8):
    print(n)

#打印结果如下：
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]

