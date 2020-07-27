"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

"""
# 使用回溯算法，主要解决这几个问题，1有没有解，2求解的具体个数和具体解，3求最优解
# 一般套路是设置一个res 和path，path保存路径， res保存结果
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(n, n, res, '')
        return res

    def dfs(self, left, right, res, path):
        if left ==0 and right ==0:
            res.append(path)
            return
        if left > 0:
            self.dfs(left-1,right,res, path + '(')
        if right > left:
            self.dfs(left, right - 1, res, path + ')')


