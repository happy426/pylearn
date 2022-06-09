"""
1.从第二个元素开始从后往前遍历，若未排序的元素比排完序的元素小，则排完序的元素往后移动，未排序的元素往前移（通过交换元素实现移动）
2.第三个元素同理，若比前面最近的元素（已排完序）大，则不动
3.重复1-2的步骤，直到最后一个元素插入成功
"""
src_list = [3, 4, 5, 8, 2, 1, 9]


def crpx(src):
    for i in range(1, len(src)):
        for j in range(i, 0, -1):
            if src[j] <= src[j-1]:
                src[j], src[j-1] = src[j-1], src[j]
        print(src)


crpx(src_list)
