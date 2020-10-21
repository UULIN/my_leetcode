# 合并两个排序的数组

def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
    """
    Do not return anything, modify A in-place instead.
    """
    if n == 0: return A
    A.remove((len(A)-n):)
    # 进行A数组遍历，将B数组的值插入A
    for i in range(m):
        # 退出条件
        if n >= 0:
            num = B.pop(0)
            n -= 1
        else:
            return A
        if num <= A[i]:
            A.insert(i,num)
        A.append(num)
          
        
        
    