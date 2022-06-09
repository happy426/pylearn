"""
最大或最小的放前面
位置找元素
"""
src = [3, 4, 5, 8, 2, 1, 9]
for i in range(len(src)-1):
    # 通过定义一个变量index来记录此时需排序的位置
    index = i
    for j in range(i+1, len(src)):
        if src[index] > src[j]:
            index = j
    # 循环结束让最小的元素与相应位置上的元素进行交换
    src[i], src[index] = src[index], src[i]
print(src)
