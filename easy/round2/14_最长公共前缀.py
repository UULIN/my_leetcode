# 最长公共字串
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    strs.sort()
    lens = len(strs)
    ans = ""
    mins = strs[0]
    maxs = strs[lens - 1]

    for i in range(len(mins)):

        if i < len(maxs) and mins[i] == maxs[i]:
            ans += mins[i]
        else:
            break

    return ans

if __name__ == '__main__':
    list = ["flower","flow","flight"]
    print(longestCommonPrefix(list))
