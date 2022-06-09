"""
1.从序列中选出一个基准数()，定义好指向序列首尾两端的两个指针（此时指针我们用下标来表示）

2.先从右下标开始查找比基准数小的元素，若下标所指向的元素 比基准数 大，则向左进一位，继续比较 直到存在比基准数小的为止，
此时便把该元素填入左下标所指向的元素（做下标第一次指向的是基准数）

3.完成 2号步骤后， 左下标需向右进一位，然后左下标进行 2号步骤类似的操作，想右遍历，查找比基准数大的元素，
找到后便把此元素填入右下表所指向的元素(注意：右下标的值已保存在左边，所以可以直接覆盖)，同理 填完后右下标相应向左移动一位，准备下一轮的操作。

4.反复执行2号和3号的操作，直至左右两下标重合，便把基准元素填入下标重合位置处，此时 基准数左右两边便完成了右边小 左边大的情况。

5.对左右两个区域单独进行上述的操作，直到区域元素个数为1为止。
"""


# 快速排序

def quick_sort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    """选取基准元素 == 挖出基准元素"""
    mid_value = alist[first]
    """定义两个 下标 (指针) 指向数列两端"""
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        """ 打破循环的条件是 左边的下标所指向的元素小于基准元素"""
        if low < high:
            alist[low] = alist[high]
        """ 赋完值后下标右进一位"""
        low += 1
    while low < high and alist[low] < mid_value:
        low += 1
        """打破循环的条件 是右边的下标所指向的元素大于基准元素"""
    if low < high:
        alist[high] = alist[low]
    """ 赋完值后下标左进一位"""
    high -= 1

    # 从大循环退出时，low == high
    """ 把基准元素插入 此时插入的位置在中间"""
    alist[low] = mid_value
    """对low左边的列表执行快速排序"""
    quick_sort(alist, first, low - 1)
    """对low右边的列表执行快速排序"""
    quick_sort(alist, low + 1, last)


# if __name__ == '__main__':
li = [0, 3, 2, 1, 5, 4, 7, 6, 10, 3]
print(li)
quick_sort(li, 0, len(li) - 1)
print(li)
