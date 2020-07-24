"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = tempnum = nums[0]
        for num in nums[1:]:
            tempnum = max(num, tempnum+ num)
            maxnum = max(maxnum, tempnum)

        return maxnum

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))