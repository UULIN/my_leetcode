def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    len_nums = len(nums)
    # 暴力法
    for i in range(len_nums - 1):
        for j in range(i+1,len_nums):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

if __name__ == '__main__':
    print(twoSum([3,2,4],6))