"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x):
        """
        取模运算
        :param x:
        :return:
        """
        old = x
        ans = 0
        if x < 0:
            return False

        while(x > 0):
            tmp = x % 10
            ans = ans * 10 + tmp
            x //= 10
        return old == ans


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome2(212))