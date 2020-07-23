"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

"""


def force(s):
    """
    暴力破解法
    :param s:
    :return:
    """
    # 如果翻转后字符串完全相等，则直接返回
    if s == s[::-1]:
        return s
    # 设定回文子串的最大长度是1，结果取第一位
    max_len = 1
    res = s[0]
    # 进行循环查找
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if j - i + 1 > max_len and s[i: j + 1] == s[i: j + 1][::-1]:
                max_len = j - i + 1
                res = s[i: j + 1]
    return res


if __name__ == '__main__':
    print(force('babad'))
