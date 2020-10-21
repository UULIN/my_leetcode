"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 设定对应的字典
        hashmap = {')': '(', '}': '{', ']': '['}
        # 用列表模拟一个栈
        stack = []
        for i in s:
            if stack and i in hashmap:
                if stack[-1] == hashmap(i):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

