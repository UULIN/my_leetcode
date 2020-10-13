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

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        思路挺无敌的
        """
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    def isValid2(self, s):
        """

        :param s:
        :return:
        用栈的方法试一下
        """
        # 先用列表模拟一个栈
        stark =[]
        # 使用字典的对应关系
        dic = {']': '[', '}': '{', ')': '('}
        # 进行字符串的遍历
        for i in s:
            if stark and i in dic: # 如果栈不为空且遍历的字符串可以在字典中找到对应关系
                if stark[-1] == dic[i]: # 后入先出的关系，如果栈顶元素与字典中对应的值相等
                    stark.pop() # 将栈顶元素抛出
                else:
                    return False
            else:
                stark.append(i)
        return not stark
