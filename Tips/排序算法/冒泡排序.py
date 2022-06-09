"""
相邻的比较
升序：左边比右边大，互换
降序：左边比右边小，互换
"""
src = [3, 4, 5, 8, 2, 1, 9]
for i in range(len(src)-1):
    for j in range(len(src)-1-i):
        if src[j] > src[j+1]:
            src[j], src[j+1] = src[j+1], src[j]
print(src)



