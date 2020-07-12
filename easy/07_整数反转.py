"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # 进行排序前的值收集
    list1 = []
    # 进行排序后的值收集
    list2 = []
    args1 = False
    # 是否是负数
    if x < 0:
        x = -x
        args1 = True

    for i in str(x):
        list1.append(i)
    m = len(list1)
    for j in range(m):
        list2.append(list1[m - j - 1])
    if list2[0] == 0:
        list2.pop(0)
    nums = int(''.join(list2))
    if args1:
        nums = -nums
    if -2 ** 31 <= nums <= 2 ** 31 - 1:
        return nums
    else:
        return 0


if __name__ == '__main__':

    print(reverse(12312312423423))


