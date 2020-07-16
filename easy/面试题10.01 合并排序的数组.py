"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m
"""

class Solution(object):
    def merge(self, A, m, B, n):

        """
        老han推车法
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        # 设定一个第三者
        sorted = []
        # 设定两个指针，pa, pb
        pa, pb = 0,0

        while pa < m or pb < n:
            # 如果pa先到达末尾，则将pb的的所有值插入进队列
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] > B[pb]:
                sorted.append(B[pb])
                pb += 1
            else:
                sorted.append(A[pa])
                pa += 1
        A[:] = sorted
        return A

if __name__ == '__main__':
    s = Solution()
    print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))